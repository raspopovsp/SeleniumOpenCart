import inspect
import logging
from pathlib import Path

def loggen(log_level=logging.DEBUG):
    # gets the name of the class or method from where this method is called
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)

    # By default, log all events
    logger.setLevel(logging.DEBUG)

    Path("./REPORTS/LOGS").mkdir(parents=True, exist_ok=True)
    logger_name = f"./REPORTS/LOGS/{logger_name.lower()}.log"
    file_handler = logging.FileHandler(logger_name.lower(), mode="a+")
    file_handler.setLevel(log_level)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                  datefmt='%m/%d/%Y %I:%M:%S %p')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger