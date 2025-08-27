
from datetime import datetime


class SingletonLogger(object):
    class _SingletonLogger():
        def __init__(self,filename):
            self.filename = filename
        def __str__(self):
            return "{0!r} appender filename {1}".format(self, self.filename)
        # the rest of the class definition will follow here, as per the previous logging script
        def _write_log(self,level,message):
            with open(self.filename, 'a') as logfile:
                logfile.write("[{}]:[{}]: {} \n".format(level, datetime.now().strftime("%y.%m.%d--%H:%M:%S"), message))
        def critical(self, message):
            self._write_log("CRITICAL", message)
        def error(self, message):
            self._write_log("ERROR", message)
        def warning(self, message):
            self._write_log("WARNING", message)
        def info(self, message):
            self._write_log("INFO", message)

    instance = None
    def __new__(cls, filename):
        if not SingletonLogger.instance:
            SingletonLogger.instance = SingletonLogger._SingletonLogger(filename)
            with open(filename, 'w') as log:
                pass
        # this will use methods in _SingletonLogger
        return SingletonLogger.instance
        # this will use methods in SingletonLogger
        # return super(SingletonObj, cls).__new__(cls)

    def __getattr__(self, name):
        return getattr(self.instance, name)
    def __setattr__(self, name):
        return setattr(self.instance, name)
    
if __name__ == '__main__':
    logger = SingletonLogger("mylog.txt")
    logger.warning("behold danger ahead")
    logger.critical("this is dangerous")
    