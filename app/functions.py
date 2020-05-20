"""General functions"""

import math


from app import MAX_OFFER


def print_player_market(market):
    """Print player market"""
    print('id     lowest         1T         2T         3T         4T         5T')
    for resource_type, offers in market.items():
        print('{:2} {:10.2f} {:10.2f} {:10.2f} {:10.2f} {:10.2f} {:10.2f}'.format(
            resource_type,
            offers[0]['price'] / 100,
            calculate_purchage_amount(offers, 1e12) / 100,
            calculate_purchage_amount(offers, 2e12) / 100,
            calculate_purchage_amount(offers, 3e12) / 100,
            calculate_purchage_amount(offers, 4e12) / 100,
            calculate_purchage_amount(offers, 5e12) / 100,
        ).replace(',', '.'))

    for resource_type, offers in market.items():
        max_offer = MAX_OFFER[resource_type]
        prices = str(resource_type)
        one_t_average = calculate_purchage_amount(offers, 1e12) / 100
        for i in range(1, 20):
            prices += ',{}'.format(
                calculate_purchage_amount(offers, i * 3 * max_offer * one_t_average) / 100,
            )
        print(prices)

def print_state_market(market):
    """Print state offers"""
    print('  id  region_id region_name')
    for item in market:
        print('{:6} {:8} {:20} {:14.2f} {:10}'.format(
            item['item_type'],
            item['region_id'],
            item['region_name'],
            item['price'] / 100,
            item['amount']
        ).replace(',', '.'))

def calculate_average_price(offers, amount):
    """Calculate average price based on amount"""
    total = calculate_price(offers, amount)
    return total / amount

def calculate_price(offers, amount):
    """Calculate price for amount"""
    tmp_amount = amount
    total_price = 0
    for offer in offers:
        buy_amount = offer['amount']
        if buy_amount > tmp_amount:
            buy_amount = tmp_amount
        tmp_amount -= buy_amount
        total_price += buy_amount * offer['price']
        if tmp_amount == 0:
            break
    return total_price

def calculate_purchage_amount(offers, money):
    """Calculate purchage amount"""
    tmp_money = money * 100
    total_amount = 0
    spend_money = 0
    for offer in offers:
        buy_amount = math.floor(tmp_money / (offer['price']))
        if buy_amount > 0:
            if buy_amount > offer['amount']:
                buy_amount = offer['amount']
            tmp_money -= buy_amount * offer['price']
            spend_money += buy_amount * offer['price']
            total_amount += buy_amount
            if tmp_money == 0:
                break
        else:
            break
    return round(spend_money / total_amount)
