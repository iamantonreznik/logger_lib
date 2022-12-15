# v0.3
# dev version

import os
import sys
from datetime import datetime


class Logger:

    def __init__(self, folder, prefix):
        self.folder = folder
        self.prefix = prefix
        if self.prefix[-1] != "_":
            self.prefix = self.prefix + "_"
        self.logfile = os.path.join(self.folder, self.prefix + datetime.today().strftime("%d-%m-%Y") + ".log")

    def __make_log_file(self):
        try:
            if not os.path.exists(self.folder):
                os.mkdir(self.folder)
        except OSError as folder_error:
            print('CREATING FOLDER ERROR: ' + folder_error.strerror + ' --> ' + folder_error.filename)
        try:
            if not os.path.exists(self.logfile):
                with open(self.logfile, "a") as f:
                    f.write('')
        except OSError as writing_error:
            print('CREATING LOG FILE ERROR: ' + writing_error.strerror + ' --> ' + writing_error.filename)
        return self.logfile

    def write(self, message):
        logfile = self.__make_log_file()
        
        try:
            with open(logfile, "a") as f:
                f.write('[ ' + datetime.today().strftime('%H:%M:%S') + ' ]  ' +
                        '[ ' + os.path.basename(sys.argv[0]) + ' ]  ' + message + '\n')

        except OSError as writing_error:
            print('WRITING ERROR: ' + writing_error.strerror + ' --> ' + writing_error.filename)

    def debug(self, message):
        logfile = self.__make_log_file()
        
        try:
            debug_message = '[ ' + datetime.today().strftime('%H:%M:%S') + ' ]  ' + \
                            '[ ' + os.path.basename(sys.argv[0]) + ' ]' + '  [ DEBUG ]  ' + message + '\n'
            with open(logfile, "a") as f:
                f.write(debug_message)

        except OSError as writing_error:
            print('WRITING ERROR: ' + writing_error.strerror + ' --> ' + writing_error.filename)

    def error(self, message):
        logfile = self.__make_log_file()
        
        try:
            error_message = '[ ' + datetime.today().strftime('%H:%M:%S') + ' ]  ' + \
                            '[ ' + os.path.basename(sys.argv[0]) + ' ]' + '  [ ERROR ]  ' + message + '\n'
            with open(logfile, "a") as f:
                f.write(error_message)

        except OSError as writing_error:
            print('WRITING ERROR: ' + writing_error.strerror + ' --> ' + writing_error.filename)

    def critical(self, message):
        logfile = self.__make_log_file()
        
        try:
            critical_message = '[ ' + datetime.today().strftime('%H:%M:%S') + ' ]  ' + \
                               '[ ' + os.path.basename(sys.argv[0]) + ' ]' + '  --> CRITICAL <--  ' + message + '\n'
            with open(logfile, "a") as f:
                f.write(critical_message)

        except OSError as writing_error:
            print('WRITING ERROR: ' + writing_error.strerror + ' --> ' + writing_error.filename)
