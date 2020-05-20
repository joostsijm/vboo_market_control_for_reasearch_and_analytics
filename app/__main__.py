"""Main app"""

import sys
import time

from app import SCHEDULER, LOGGER, jobs


if __name__ == '__main__':
    jobs.update_resource_market()

    LOGGER.info('Starting application')
    SCHEDULER.add_job(
        jobs.update_resource_market,
        'cron',
        id='job_update_resource_market',
        replace_existing=True,
        minute='0,10,20,30,40,50'
        # minute='0,5,10,15,20,25,30,35,40,45,50,55'
    )

    try:
        while True:
            time.sleep(100)
    except KeyboardInterrupt:
        LOGGER.info('Exiting application')
        SCHEDULER.shutdown()
        sys.exit()
