"""Jobs for scheduler module"""

from app import app

def update_resource_market():
    """job for update resource market"""
    app.update_resource_market()

