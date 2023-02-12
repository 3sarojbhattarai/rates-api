"""
    Setup for logger
"""

import os
import logging

# Gets or creates a logger
logger = logging.getLogger(__name__)

# set log level
logger.setLevel(logging.DEBUG)

# define file handler and set formatter
if not os.path.exists('./logs/'):
    os.makedirs('./logs/')
file_handler = logging.FileHandler('logs/rateapi.log')

formatter = logging.Formatter(
    '%(levelname)s [%(asctime)s] %(process)d/%(thread)d %(filename)s %(funcName)s : %(message)s')
file_handler.setFormatter(formatter)

# add file handler to logger
logger.addHandler(file_handler)
