# Simple logger library
# author Anton Reznik
# https://github.com/iamantonreznik/logger_lib
# version 0.3
# MIT license
#
# usage:
# import logger_lib
# mylogger = logger_lib.Logger(dir, prefix)
# # use directory for logs instead of dir, e.g. 'logs'
# # use prefix for each log file instead of prefix, e.g. 'log_'
#
# mylogger.write('Simple message with [ INFO ] tag')
# mylogger.debug('Message with [ DEBUG ] tag')
# mylogger.error('Message with [ ERROR ] tag')
# mylogger.critical('Message with --> CRITICAL <-- tag')

import os
import sys
import inspect
from datetime import datetime


class Logger:

    def __init__(self, folder, prefix):
        self.folder = folder
        self.prefix = prefix
        if self.prefix[-1] != "_":
            self.prefix = self.prefix + "_"
        self.logfile = os.path.join(self.folder, self.prefix + datetime.today().strftime("%d-%m-%Y") + ".log")

    def __exception_worker(function):
        def inner_function(self, *args, **kwargs):
            callerframerecord = inspect.stack()[-1]
            frame = callerframerecord[0]
            info = inspect.getframeinfo(frame)

            try:
                function(self, *args, **kwargs)

            except TypeError:
                print('[' + os.path.basename(sys.argv[0]) + '] [ line: ' + str(info.lineno)
                      + ' ] logger_lib usage error --> ' + str(info.code_context[0].removesuffix('\n')))

            except OSError as logger_error:
                print('[' + os.path.basename(sys.argv[0]) + '] [ line: ' + str(info.lineno)
                      + ' ] logger_lib writing error: ' + logger_error.strerror +
                      ' --> ' + logger_error.filename)

        return inner_function

    @__exception_worker
    def __make_log_file(self):
        logfile = self.logfile

        if not os.path.exists(self.folder):
            os.makedirs(self.folder)
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

    @__exception_worker
    def write(self, message):
        """
        function for write simple info messages
        Returns [ time ]  [ file ]  [ INFO ]  message
        Args:
            message: message to write
        """
        self.__make_log_file()

        with open(self.logfile, "a") as f:
            f.write(self.__message_worker('info', message))

    @__exception_worker
    def debug(self, message):
        """
        function for write debug messages
        Returns [ time ]  [ file ]  [ DEBUG ]  message
        Args:
            message: message to write
        """
        self.__make_log_file()
        with open(self.logfile, "a") as f:
            f.write(self.__message_worker('debug', message))

    @__exception_worker
    def error(self, message):
        """
        function for write error messages
        Returns [ time ]  [ file ]  [ ERROR ]  message
        Args:
            message: message to write
        """
        self.__make_log_file()
        with open(self.logfile, "a") as f:
            f.write(self.__message_worker('error', message))

    @__exception_worker
    def critical(self, message):
        """
        function for write critical messages
        Returns [ time ]  [ file ]  --> CRITICAL <--  message
        Args:
            message: message to write
        """
        self.__make_log_file()
        with open(self.logfile, "a") as f:
            f.write(self.__message_worker('critical', message))
