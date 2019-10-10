"""general methods"""

import math

from app import MAX_OFFER

def print_offers(market):
    """Print offers"""
    print('id     lowest       0.5T         1T         2T         5T')
    for resource_type, offers in market.items():
        print('{:2} {:10.2f} {:10.2f} {:10.2f} {:10.2f} {:10.2f}'.format(
            resource_type,
            offers[0]['price'] / 100,
            calculate_purchage_amount(offers, 5e11) / 100,
            calculate_purchage_amount(offers, 1e12) / 100,
            calculate_purchage_amount(offers, 2e12) / 100,
            calculate_purchage_amount(offers, 5e12) / 100,
        ).replace(',', '.'))

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
    for offer in offers:
        buy_amount = math.floor(tmp_money / (offer['price']))
        if buy_amount > 0:
            if buy_amount > offer['amount']:
                buy_amount = offer['amount']
            tmp_money -= buy_amount * (offer['price'])
            total_amount += buy_amount
            if tmp_money == 0:
                break
        else:
            break
    return round(money * 100 / total_amount)
