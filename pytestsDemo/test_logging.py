import logging


def test_loggingDemo():
    logger = logging.getLogger(__name__)
    fileHandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)  # we have to pass file handler object into it. File handler is file location.

    logger.setLevel(logging.INFO)
    # NOTE : if we set the level to DEBUG then below that all Info, warning, error and critical
    # levels will be printed in the log file.

    logger.debug("DEBUG statement is executed")
    logger.info("INFORMATION statement is executed")
    logger.warning("WARNING statement is executed")
    logger.error("ERROR statement is executed")
    logger.critical("CRITICAL statement is executed")
