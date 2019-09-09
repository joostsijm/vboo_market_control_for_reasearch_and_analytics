"""API module"""

import requests
from bs4 import BeautifulSoup

from app import BASE_URL, HEADERS, ITEMS


def get_player_market():
    """Get player market"""
    # return read_player_market()
    return download_player_market()

def read_player_market():
    """Read player_market"""
    with open('item.html') as file:
        return [parse_item(file)]

def download_player_market():
    """Download the market"""
    items = []
    for item_id in ITEMS.values():
        print(item_id)
        response = requests.get(
            '{}storage/market/{}'.format(BASE_URL, item_id),
            headers=HEADERS
        )
        items.append(parse_item(response.text))
    return items

def parse_item(html):
    """Parse html return item"""
    soup = BeautifulSoup(html, 'html.parser')
    print(soup.find(class_='storage_buy_button'))
    return {
        'player_id': int(soup.find(class_='storage_buy_button')['whose']),
        'player_name': soup.select_one('.storage_see.dot').string,
        'price': int(soup.find(class_='storage_buy_input')['price']),
        'amount': int(soup.find(class_='storage_market_number')['max']),
        'total_offers': int(soup.select_one('.storage_see').string),
        'item_type': int(soup.find(class_='storage_market_number')['url']),
    }
