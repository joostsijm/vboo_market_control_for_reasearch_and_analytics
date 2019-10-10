"""Main app"""

import time

from app import SCHEDULER, LOGGER
from app.api import get_player_market, get_state_market
from app.database import save_resource_market


def job_update_resource_market():
    """Update market"""
    LOGGER.info('Get player market')
    player_market = get_player_market()
    LOGGER.info('Got player market')
    # print_offers(player_market)

    LOGGER.info('Get state market')
    state_market = get_state_market()
    LOGGER.info('Got state market')
    # print(state_market)

    LOGGER.info('saving markets')
    save_resource_market(player_market, state_market)
    LOGGER.info('done saving markets')

if __name__ == '__main__':
    job_update_resource_market()

    # job
    SCHEDULER.add_job(
        job_update_resource_market,
        'cron',
        id='job_update_resource_market',
        replace_existing=True,
        minute='0,10,20,30,40,50'
    )

    try:
        while True:
            time.sleep(100)
    except KeyboardInterrupt:
        LOGGER.info('Exiting application')
        SCHEDULER.shutdown()
        exit()
