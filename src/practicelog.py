import logging

def get_logger(logname):
    """
    param: 
        logger desired name,
        error log file path
        debug log file path
    type: str, str, str
    return: logger with 2 handlers
    type: logging.Logger
    """
    logger = logging.getLogger(logname)
    logger.setLevel(logging.DEBUG)

    error_file_handler = logging.FileHandler('logs/practice_errors.log')
    error_file_handler.setLevel(logging.ERROR)
    formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
    error_file_handler.setFormatter(formatter)

    debug_file_handler = logging.FileHandler('logs/practice_debug.log')
    debug_file_handler.setLevel(logging.DEBUG) 
    formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
    debug_file_handler.setFormatter(formatter)

    logger.addHandler(error_file_handler)
    logger.addHandler(debug_file_handler)
    return logger