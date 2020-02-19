"""Implements helper functions for the weather API requests."""

import datetime
import random

def obj_to_dict(news_obj):
    """Convert PyMongo news object to dictionary representation"""
    json = {}

    for key in news_obj.keys():
        if key == '_id':
            json[key] = str(news_obj[key])
        else:
            json[key] = news_obj[key]

    return json

def is_valid_news(news_dict):
    """Checks if a dictionary is has valid keys and values.

    Args:
        news_dict (dictionary): a dictionary that represents news

    Return:
        True if news_dict is valid news, otherwise returns False
    """
    #TODO: implement this
    return True

def is_valid_postal(postal_code):
    """Returns True if postal code is valid, otherwise returns False."""
    # TODO: implement this
    return True

def snow_day_proba(postal_code):
    day_of_week = datetime.datetime.today().weekday() # 0=Monday, ...,6=Sun

    # If day of the week is Fri or Sat, then tomorrow is not a school day
    if day_of_week == 4 or day_of_week == 5:
        return -1
    else:
        return random.randint(0,100)