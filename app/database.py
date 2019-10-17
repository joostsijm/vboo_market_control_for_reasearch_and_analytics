"""Database module"""

from datetime import datetime

from app import SESSION
from app.models import State, Region, Player, MarketTrack, StateMarketStat, PlayerMarketStat
from app.app import calculate_purchage_amount


def get_new_market_track(session, resources, state_resources, items):
    """Get ner market track"""
    market_track = MarketTrack()
    market_track.date_time = datetime.now()
    market_track.resources = resources
    market_track.state_resources = state_resources
    market_track.items = items
    session.add(market_track)
    return market_track

def save_resource_market(player_market, state_market):
    """Save factories to database"""
    session = SESSION()

    market_track = get_new_market_track(session, True, True, False)
    market_track.player_resources = True
    market_track.state_resources = True
    _save_player_market(session, market_track, player_market)
    _save_state_market(session, market_track, state_market)

    session.commit()
    session.close()

def save_player_market(market):
    """Save player market"""
    session = SESSION()
    market_track = get_new_market_track(session, True, False, False)
    session.add(market_track)
    _save_player_market(session, market_track, market)

def _save_player_market(session, market_track, market):
    """Save player market to database"""
    for item_type, offers in market.items():
        if offers:
            item_dict = offers[0]
            market_stat = PlayerMarketStat()
            player = session.query(Player).get(item_dict['player_id'])
            if not player:
                player = save_player(session, item_dict)
            market_stat.player_id = player.id
            market_stat.item_type = item_type
            market_stat.amount = item_dict['amount']
            market_stat.price = item_dict['price']

            market_stat.total_offers = len(offers)
            market_stat.half_t_average = calculate_purchage_amount(offers, 5e11)
            market_stat.one_t_average = calculate_purchage_amount(offers, 1e12)
            market_stat.two_t_average = calculate_purchage_amount(offers, 2e12)
            market_stat.five_t_average = calculate_purchage_amount(offers, 5e12)
            market_stat.market_track_id = market_track.id
            session.add(market_stat)

def _save_state_market(session, market_track, market):
    """Save state market"""
    for item_dict in market:
        market_stat = StateMarketStat()
        region = session.query(Region).get(item_dict['region_id'])
        if not region:
            region = save_region(session, item_dict)
        market_stat.region_id = region.id
        market_stat.market_track_id = market_track.id
        market_stat.item_type = item_dict['item_type'] - 1000
        market_stat.amount = item_dict['amount']
        market_stat.price = item_dict['price']
        session.add(market_stat)

def save_player(session, item_dict):
    """Save player to database"""
    player = Player()
    player.id = item_dict['player_id']
    player.name = item_dict['player_name']
    session.add(player)
    return player

def save_region(session, item_dict):
    """Save player to database"""
    region = Region()
    region.id = item_dict['region_id']
    region.name = item_dict['region_name']
    session.add(region)
    return region
