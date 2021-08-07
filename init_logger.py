import logging


def init_logger():
    """
    This function initialize the logger and returns its handle
    :return:
    """
    logformatter = logging.Formatter('%(levelname)s-%(asctime)s-FUNC:%(funcName)s-LINE:%(lineno)d-'
                                     ' %(message)s')
    logger = logging.getLogger('log')
    logger.setLevel('DEBUG')
    file_handler = logging.FileHandler('log.txt')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logformatter)
    logger.addHandler(file_handler)

    return logger
