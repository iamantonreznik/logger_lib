import configparser
import os
import sys
from datetime import datetime

# READ CONFIG FILE
config = configparser.ConfigParser()
config.read("logger.cfg")

# READ VARIABLES
logfilefolder = config["logger_lib"]["logfilefolder"]
logfileprefix = config["logger_lib"]["logfileprefix"]
logfileextension = config["logger_lib"]["logfileextension"]
logfilename_dateformat = config["logger_lib"]["logfilename_dateformat"]
logfile_timeformat = config["logger_lib"]["logfile_timeformat"]
maxlogfilesize = config["logger_lib"]["maxlogfilesize"]

if logfilefolder[-1] != "/":
    logfilefolder = logfilefolder + "/"


class Logger():

    def __init__(self):
        self.indexfilenumber = 0

    def checklogfile(self):
        global logfile
        indexfilenumber = 0
        logfile = logfilefolder + logfileprefix + datetime.today().strftime(logfilename_dateformat) + '_' + str(indexfilenumber) + logfileextension
        if os.path.exists(logfile) and int('%2.0f' % (os.path.getsize(logfile) / 1024)) >= int(maxlogfilesize):
            while os.path.exists(logfile):
                indexfilenumber += 1
                logfile = logfilefolder + logfileprefix + datetime.today().strftime(logfilename_dateformat) + '_' + str(indexfilenumber) + logfileextension
                if os.path.exists(logfile) and int('%2.0f' % (os.path.getsize(logfile) / 1024)) < int(maxlogfilesize):
                    return logfile
        else:
            if not os.path.exists(logfilefolder):
                os.mkdir(logfilefolder)
            with open(logfile, "a") as f:
                f.write('')
            return logfile
        return logfile

    def write(self, message):
        self.checklogfile()
        with open(logfile, "a") as f:
            f.write('[ ' + datetime.today().strftime(logfile_timeformat) + ' ]  ' + '[ ' + os.path.basename(sys.argv[0]) + ' ]  ' + message + '\n')

    def debug(self, message):
        self.checklogfile()
        debugmessage = '[ ' + datetime.today().strftime(logfile_timeformat) + ' ]  ' + '[ ' + os.path.basename(sys.argv[0]) + ' ]' + '  [ DEBUG ]  ' + message + '\n'
        with open(logfile, "a") as f:
            f.write(debugmessage)

    def error(self, message):
        self.checklogfile()
        errormessage = '[ ' + datetime.today().strftime(logfile_timeformat) + ' ]  ' + '[ ' + os.path.basename(sys.argv[0]) + ' ]' + '  [ ERROR ]  ' + message + '\n'
        with open(logfile, "a") as f:
            f.write(errormessage)

    def crit(self, message):
        self.checklogfile()
        criticalmessage = '[ ' + datetime.today().strftime(logfile_timeformat) + ' ]  ' + '[ ' + os.path.basename(sys.argv[0]) + ' ]' + '  --> CRITICAL <--  ' + message + '\n'
        with open(logfile, "a") as f:
            f.write(criticalmessage)
