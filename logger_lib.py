# v0.3
# dev version

import os
import sys
import inspect
from datetime import datetime


def exception_worker(function):
    def inner_function(*args, **kwargs):
        callerframerecord = inspect.stack()[-1]
        frame = callerframerecord[0]
        info = inspect.getframeinfo(frame)

        try:
            function(*args, **kwargs)

        except TypeError:
            print('[' + os.path.basename(sys.argv[0]) + '] [ line: ' + str(info.lineno)
                  + ' ] logger_lib usage error --> ' + str(info.code_context[0].removesuffix('\n')))

        except OSError as logger_error:
            print('[' + os.path.basename(sys.argv[0]) + '] [ line: ' + str(info.lineno)
                  + ' ] logger_lib writing error: ' + logger_error.strerror +
                  ' --> ' + logger_error.filename)

    return inner_function


class Logger:

    def __init__(self, folder, prefix):
        self.folder = folder
        self.prefix = prefix
        if self.prefix[-1] != "_":
            self.prefix = self.prefix + "_"
        self.logfile = os.path.join(self.folder, self.prefix + datetime.today().strftime("%d-%m-%Y") + ".log")

    @exception_worker
    def __make_log_file(self):
        logfile = self.logfile

        if not os.path.exists(self.folder):
            os.mkdir(self.folder)
        if not os.path.exists(self.logfile):
            with open(self.logfile, "a") as f:
                f.write('')

        return logfile

    def __message_worker(self, level, message):
        message_levels = {'info':     '  [ INFO ]  ',
                          'debug':    '  [ DEBUG ]  ',
                          'error':    '  [ ERROR ]  ',
                          'critical': '  --> CRITICAL <--  '}

        log_message = '[ ' + datetime.today().strftime('%H:%M:%S') + ' ]  ' + \
                      '[ ' + os.path.basename(sys.argv[0]) + ' ]' + message_levels[level] + message + '\n'
        return log_message

    @exception_worker
    def write(self, message):
        self.__make_log_file()

        with open(self.logfile, "a") as f:
            f.write(self.__message_worker('info', message))

    @exception_worker
    def debug(self, message):
        self.__make_log_file()
        with open(self.logfile, "a") as f:
            f.write(self.__message_worker('debug', message))

    @exception_worker
    def error(self, message):
        self.__make_log_file()
        with open(self.logfile, "a") as f:
            f.write(self.__message_worker('error', message))

    @exception_worker
    def critical(self, message):
        self.__make_log_file()
        with open(self.logfile, "a") as f:
            f.write(self.__message_worker('critical', message))
