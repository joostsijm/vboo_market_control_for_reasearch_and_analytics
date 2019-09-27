"""general methods"""

import math

from app import MAX_OFFER

def print_offers(market):
    """Print offers"""
    for resource_type, offers in market.items():
        purchage_money = 2e12
        purchage_average = calculate_purchage_amount(offers, purchage_money)
        money = MAX_OFFER[resource_type] * 5
        price = calculate_price(offers, money)
        print('{:2} {:15,} {:25,} {:15,}'.format(
            resource_type, 
            purchage_average / 100,
            price,
            offers[0]['price'] / 100,
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
