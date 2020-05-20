"""general methods"""

from app import LOGGER, api, database, functions


def update_resource_market():
    """update resource market"""
    LOGGER.info('Get player market')
    player_market = api.get_player_market()
    LOGGER.info('Got player market')
    functions.print_player_market(player_market)

    LOGGER.info('Get state market')
    state_market = api.get_state_market()
    LOGGER.info('Got state market')
    functions.print_state_market(state_market)

    LOGGER.info('saving markets')
    database.save_resource_market(player_market, state_market)
    LOGGER.info('done saving markets')
