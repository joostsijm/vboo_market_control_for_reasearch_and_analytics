"""API module"""

import re

import requests
from bs4 import BeautifulSoup

from app import BASE_URL, HEADERS, RESOURCES, ITEMS, STATE_ITEMS


def download_item(item_type):
    """Download item id"""
    html = ''
    while not html:
        response = requests.get(
            '{}storage/market/{}'.format(BASE_URL, item_type),
            headers=HEADERS
        )
        html = response.text
    return html

def download_offers(item_type):
    """Download item id"""
    html = ''
    while not html:
        response = requests.get(
            '{}storage/listed/{}'.format(BASE_URL, item_type),
            headers=HEADERS
        )
        html = response.text
    return html

def get_player_market():
    """Get player market"""
    # return read_player_market()
    return download_player_market()

def read_player_market():
    """Read player market"""
    with open('items.html') as file:
        resources = {}
        for resource_type in RESOURCES.values():
            resources[resource_type] = parse_player_offers(file)
            break
        return resources

def download_player_market():
    """Download the market"""
    resources = {}
    for resource_type in RESOURCES.values():
        html = download_offers(resource_type)
        resources[resource_type] = parse_player_offers(html)
    return resources

def parse_player_item(html, item_type):
    """Parse html return player item"""
    soup = BeautifulSoup(html, 'html.parser')
    return {
        'player_id': int(re.sub(r'^.*\/', '', soup.select_one('.storage_see.dot')['action'])),
        'player_name': soup.select_one('.storage_see.dot').string,
        'price': int(float(soup.find(class_='storage_buy_input')['price'])*100),
        'amount': int(soup.find(class_='storage_market_number')['max']),
        'total_offers': int(re.sub(r'\..*$', '', soup.select_one('.storage_see').string)),
        'item_type': item_type,
    }

def parse_player_offers(html):
    """Parse html return player item"""
    soup = BeautifulSoup(html, 'html.parser')
    offers_tree = soup.find_all(class_='list_link')
    offers = []
    for offer_tree in offers_tree:
        offers.append({
            'player_id': int(re.sub(r'^.*\/', '', offer_tree.select_one('.results_date')['action'])),
            'player_name': offer_tree.select_one('.results_date').string,
            'price': int(float(offer_tree.select('.list_level')[1]['rat'])*100),
            'amount': int(offer_tree.select_one('.list_level.imp.small')['rat']),
        })
    return offers

def get_state_market():
    """Get state market"""
    # return read_state_market()
    return download_state_market()

def read_state_market():
    """Read state market"""
    with open('state_item.html') as file:
        return [parse_state_item(file, 1001)]

def download_state_market():
    """Download the state market"""
    items = []
    for item_type in STATE_ITEMS.values():
        item = download_item(item_type)
        items.append(parse_state_item(item, item_type))
    return items

def parse_state_item(html, item_type):
    """Parse htm return state item"""
    soup = BeautifulSoup(html, 'html.parser')
    return {
        'region_id': int(re.sub(r'^.*\/', '', soup.select_one('.storage_see.dot')['action'])),
        'region_name': soup.select_one('.storage_see.dot').string,
        'price': int(float(soup.find(class_='storage_buy_input')['price'])*100),
        'amount': int(soup.find(class_='storage_market_number')['max']),
        'item_type': item_type,
    }
