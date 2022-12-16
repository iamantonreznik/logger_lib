# v0.3
# dev version

import os
import sys
from datetime import datetime


def exception_handler(function):
    def inner_function(*args, **kwargs):
        try:
            function(*args, **kwargs)
        except OSError as logger_error:
            print('[' + os.path.basename(sys.argv[0]) + '] logger_lib writing error: '
                  + logger_error.strerror + ' --> ' + logger_error.filename)

    return inner_function


class Logger:

    def __init__(self, folder, prefix):
        self.folder = folder
        self.prefix = prefix
        if self.prefix[-1] != "_":
            self.prefix = self.prefix + "_"
        self.logfile = os.path.join(self.folder, self.prefix + datetime.today().strftime("%d-%m-%Y") + ".log")

    @exception_handler
    def __make_log_file(self):

        if not os.path.exists(self.folder):
            os.mkdir(self.folder)
        if not os.path.exists(self.logfile):
            with open(self.logfile, "a") as f:
                f.write('')

        # return self.logfile

    def __message_worker(self, level, message):
        message_levels = {'info': '  [ INFO ]  ',
                          'debug': '  [ DEBUG ]  ',
                          'error': '  [ ERROR ]  ',
                          'critical': '  --> CRITICAL <--  '}

        log_message = '[ ' + datetime.today().strftime('%H:%M:%S') + ' ]  ' + \
                      '[ ' + os.path.basename(sys.argv[0]) + ' ]' + message_levels[level] + message + '\n'
        return log_message

    @exception_handler
    def write(self, message):
        self.__make_log_file()

        with open(self.logfile, "a") as f:
            f.write(self.__message_worker('info', message))

    @exception_handler
    def debug(self, message):
        self.__make_log_file()

        with open(self.logfile, "a") as f:
            f.write(self.__message_worker('debug', message))

    @exception_handler
    def error(self, message):
        self.__make_log_file()

        with open(self.logfile, "a") as f:
            f.write(self.__message_worker('error', message))

    @exception_handler
    def critical(self, message):
        self.__make_log_file()

        with open(self.logfile, "a") as f:
            f.write(self.__message_worker('critical', message))
