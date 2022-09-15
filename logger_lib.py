from datetime import datetime


class Logger():

    def __init__(self):
        self.logfile = 'log_' + str(datetime.now().date()) + '.txt'

    def write(self, message):
        with open(self.logfile, "a") as f:
            f.write(message + '\n')
