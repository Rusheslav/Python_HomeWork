import logging

logging.basicConfig(
    level=logging.INFO,
    filename="mylog.log",
    format="%(asctime)s - %(funcName)s: %(lineno)d - %(message)s",
    datefmt='%H:%M:%S'
)