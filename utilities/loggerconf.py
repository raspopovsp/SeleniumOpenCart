import logging

log_format = f"%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"


class LogGen:

    @staticmethod
    def get_file_handler():
        file_handler = logging.FileHandler("./REPORTS/LOGS/log.log")
        file_handler.setLevel(logging.WARN)
        file_handler.setFormatter(logging.Formatter(log_format))
        return file_handler

    @staticmethod
    def get_stream_handler():
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        stream_handler.setFormatter(logging.Formatter(log_format))
        return stream_handler

    @staticmethod
    def loggen(name):
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)
        fh = LogGen.get_file_handler()
        sh = LogGen.get_stream_handler()
        logger.addHandler(fh)
        logger.addHandler(sh)

        return logger
