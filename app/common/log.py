import logging
from logging.handlers import TimedRotatingFileHandler, HTTPHandler


def setup_logger(log_path, logger_name, log_file, level=logging.INFO, format='%(lineno)d %(asctime)s %(message)s'):
    log_setup = logging.getLogger(logger_name)
    formatter = logging.Formatter(format, datefmt='%Y-%m-%d %H:%M:%S')
    file_handler = TimedRotatingFileHandler(filename='%s/%s' % (log_path, log_file),
                                            when="D", interval=1, backupCount=20)

    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    http_handle = HTTPHandler(host='', url='', method='POST')
    http_handle.setFormatter(formatter)

    log_setup.setLevel(level)
    log_setup.addHandler(file_handler)
    log_setup.addHandler(stream_handler)





