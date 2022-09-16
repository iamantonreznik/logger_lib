from datetime import datetime
import configparser
import os


# READ CONFIG FILE
config = configparser.ConfigParser()
config.read("logger.cfg")

# READ VARIABLES
logfileprefix = config["logger_lib"]["logfileprefix"]
logfileextension = config["logger_lib"]["logfileextension"]
logfilename_dateformat = config["logger_lib"]["logfilename_dateformat"]
logfile_timeformat = config["logger_lib"]["logfile_timeformat"]
maxlogfilesize = config["logger_lib"]["maxlogfilesize"]

startmessage =    '|--------------------------------------|\n' \
                  '|          logger_lib started          |\n' \
                  '|          ' + datetime.today().strftime("%d-%m-%Y %H:%M:%S") +  '         |\n' \
                  '\n'
endmessage =      '\n' \
                  '|          logger_lib stopped          |\n' \
                  '|--------------------------------------|\n\n'

class Logger():

    def __init__(self):
        self.indexnumber = 1
        self.indexfilenumber = 0

    def checkLogfile(self):
        global logfile
        indexfilenumber = 0
        logfile = logfileprefix + datetime.today().strftime(logfilename_dateformat) + '_' + str(indexfilenumber) + logfileextension
        if os.path.exists(logfile) and int('%2.0f' % (os.path.getsize(logfile) / 1024)) >= int(maxlogfilesize):
            while os.path.exists(logfile):
                indexfilenumber += 1
                logfile = logfileprefix + datetime.today().strftime(logfilename_dateformat) + '_' + str(indexfilenumber) + logfileextension
                if os.path.exists(logfile) and int('%2.0f' % (os.path.getsize(logfile) / 1024)) < int(maxlogfilesize):
                    return logfile
            else:
                with open(logfile, "a") as f:
                    f.write('')
                return logfile
        return logfile

    def startLogging(self):
        self.checkLogfile()
        with open(logfile, "a") as f:
            f.write(startmessage)

    def write(self, message):
        self.checkLogfile()
        with open(logfile, "a") as f:
            f.write('[ ' + str('%03d' % (self.indexnumber)) + ' ]  ' + datetime.today().strftime(logfile_timeformat) + '  ' + message + '\n')
            self.indexnumber += 1

    def __del__(self):
        with open(logfile, "a") as f:
            f.write(endmessage)
