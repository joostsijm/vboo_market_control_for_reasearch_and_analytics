"""Database module"""

from datetime import datetime

from app import Session
from app.models import State, Region, Player, MarketTrack, StateMarketStat, PlayerMarketStat


def save_market(player_market, state_market):
    """Save factories to database"""
    session = Session()
    session.close()

    market_track = MarketTrack()
    market_track.date_time = datetime.now()
    session.add(market_track)

    for item_dict in player_market:
        player_market_stat = PlayerMarketStat()
        player = session.query(Player).get(item_dict['player_id'])
        if not player:
            player = save_player(session, item_dict)
        player_market_stat.player_id = player.id
        player_market_stat.item_type = item_dict['item_type']
        player_market_stat.total_offers = item_dict['total_offers']
        player_market_stat.amount = item_dict['amount']
        player_market_stat.price = item_dict['price']
        player_market_stat.market_track_id = market_track.id
        session.add(player_market_stat)

    session.commit()
    session.close()

def save_player(session, item_dict):
    """Save player to database"""
    player = Player()
    player.id = item_dict['player_id']
    player.name = item_dict['player_name']
    session.add(player)
    return player
