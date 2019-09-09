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
engine = create_engine(os.environ["DATABASE_URI"], client_encoding='utf8')
Session = sessionmaker(bind=engine)

# scheduler
scheduler = BackgroundScheduler()
scheduler.start()

# logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
LOGGER = logging.getLogger(__name__)

# api
BASE_URL = os.environ["API_URL"]
HEADERS = {
    'Authorization': os.environ["AUTHORIZATION"]
}

# misc
ITEMS = {
    'oil': 3,
    'ore': 4,
    'uranium': 11,
    'diamond': 15,
    'liquid oxygen': 21,
    'helium-3': 24,
    'antirad': 13,
    'spacerockets': 20,
    'tanks': 2,
    'aircrafts': 1,
    'missiles': 14,
    'bombers': 16,
    'battleships': 18,
    'moon tanks': 22,
    'space stations': 23
}
