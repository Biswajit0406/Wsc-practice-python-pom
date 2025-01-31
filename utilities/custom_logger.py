import logging

class Log_maker:
    @staticmethod
    def log_gen():
        logging.basicConfig(filename="C:/Users/KIIT/PycharmProjects/pythonProject1/logs/wsc.log",format='%(asctime)s:%(levelname)s:%(message)s',datefmt="%Y-%m-%d %H:%M:%S",force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

