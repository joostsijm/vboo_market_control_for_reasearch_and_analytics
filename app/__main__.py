"""Main app"""

import time

from app import scheduler, LOGGER
from app.api import get_player_market #, get_state_market
from app.database import save_market


def print_player_market(player_market):
    """Print player market"""
    for item in player_market:
        print('{:3} {:5}'.format(
            item['id'],
            item['price'],
        ))

def job_update_market():
    """Update market"""
    LOGGER.info('Get player market')
    player_market = get_player_market()
    LOGGER.info('Got player market')
    print(player_market)

    LOGGER.info('Get state market')
    # state_market = get_state_market()
    LOGGER.info('Got state market')

    # print_market(factories)
    LOGGER.info('saving markets')
    save_market(player_market, [])
    LOGGER.info('done saving markets')

if __name__ == '__main__':
    job_update_market()

    # job
    scheduler.add_job(
        job_update_market,
        'cron',
        id='update_market',
        replace_existing=True,
        minute='0,10,20,30,40,50'
    )

    try:
        while True:
            time.sleep(100)
    except KeyboardInterrupt:
        LOGGER.info('Exiting application')
        exit()
