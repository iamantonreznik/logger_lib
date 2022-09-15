from datetime import datetime
import configparser


# READ CONFIG FILE
config = configparser.ConfigParser()
config.read("config.cfg")

# READ VARIABLES
logfilename = config["logger_lib"]["logfilename"]
logfilename_dateformat = config["logger_lib"]["logfilename_dateformat"]
logfile_timeformat = config["logger_lib"]["logfile_timeformat"]

startmessage = '\n' \
               '|--------------------------------------|\n' \
               '|          logger_lib started          |\n' \
               '|          ' + datetime.today().strftime("%d-%m-%Y %H:%M:%S") +  '         |\n' \
               '|--------------------------------------|\n\n'

class Logger():

    def __init__(self):
        self.logfile = logfilename + datetime.today().strftime(logfilename_dateformat) + '.txt'

    def startLogging(self):
        with open(self.logfile, "a") as f:
            f.write(startmessage)

    def write(self, message):
        with open(self.logfile, "a") as f:
            f.write(datetime.today().strftime(logfile_timeformat)+ '   ' + message + '\n')
