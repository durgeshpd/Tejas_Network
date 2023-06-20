import logging


class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger("Test Cases for Supervisor Role")
        file_handler = logging.FileHandler("log_file.log", mode="a")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.INFO)
        return logger
