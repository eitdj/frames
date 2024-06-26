import logging


class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename='\\logs\\automation.log', format='%(as)23.55sec')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
