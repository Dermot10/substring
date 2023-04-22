import logging 

#Logger instance instantiated to allow program to produce log messages 

#create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

#create file handler
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)

#create formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

