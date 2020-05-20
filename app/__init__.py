"""Markt Controle voor Onderzoek en Analyse"""

import os
import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from apscheduler.schedulers.background import BackgroundScheduler

from app.models import Base, State, Region, Player


load_dotenv()

# database
ENGINE = create_engine(os.environ["DATABASE_URI"], client_encoding='utf8')
SESSION = sessionmaker(bind=ENGINE)

# scheduler
SCHEDULER = BackgroundScheduler(
    daemon=True,
    job_defaults={'misfire_grace_time': 5*60},
    max_instances=5,
)
SCHEDULER.start()

# get logger
LOGGER = logging.getLogger('mcoa')
LOGGER.setLevel(logging.DEBUG)
SCHEDULER_LOGGER = logging.getLogger('apscheduler')
SCHEDULER_LOGGER.setLevel(logging.DEBUG)

# create file handler
FILE_HANDLER = logging.FileHandler('output.log')
FILE_HANDLER.setLevel(logging.DEBUG)

# create console handler
STREAM_HANDLER = logging.StreamHandler()
STREAM_HANDLER.setLevel(logging.INFO)

# create formatter and add it to the handlers
FORMATTER = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
STREAM_HANDLER.setFormatter(FORMATTER)
FILE_HANDLER.setFormatter(FORMATTER)

# add the handlers to logger
LOGGER.addHandler(STREAM_HANDLER)
LOGGER.addHandler(FILE_HANDLER)
SCHEDULER_LOGGER.addHandler(STREAM_HANDLER)
SCHEDULER_LOGGER.addHandler(FILE_HANDLER)

# api
BASE_URL = os.environ["API_URL"]
HEADERS = {
    'Authorization': os.environ["AUTHORIZATION"]
}

# misc
RESOURCES = {
    'oil': 3, 'ore': 4, 'uranium': 11, 'diamond': 15,
}

ITEMS = {
    'liquid oxygen': 21, 'helium-3': 24, 'rivalium': 26, 'antirad': 13,
    'spacerockets': 20, 'lss': 25, 'tanks': 2,
    'aircrafts': 1, 'missiles': 14, 'bombers': 16, 'battleships': 18,
    'laser drones': 27, 'moon tanks': 22, 'space stations': 23
}

STATE_ITEMS = {
    'gold': 1000, 'oil': 1003, 'ore': 1004, 'uranium': 1011,
    'diamond': 1015,
}

MAX_OFFER = {
    3: 614400000, 4: 614400000, 11: 15360000, 15: 153600,
    21: 38400000, 24: 153600, 26: 614400, 13: 76800,
    20: 3840, 25: 15360000, 2: 4388571,
    1: 640000, 14: 256000, 16: 128000, 18: 128000,
    27: 256000, 22: 12800, 23: 1280
}
