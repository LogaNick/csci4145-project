"""Implements helper functions for the weather API requests."""

import datetime
import random

#unused now, delete if still unused in final version
def str_to_date(date_string):
    """Convert str to date object

    Args:
        a string in YYYY-mm-dd format

    Returns:
        a date object
    """
    date = datetime.datetime.strptime(date_string, "%Y-%m-%d").date()
    return date

def obj_to_dict(obj):
    """Convert PyMongo object to dictionary representation

    Args:
        # TODO: figure out what this type is and look into whether it has a built in to_dict/to_json method.
        obj (dictionary-like PyMongo type?): a PyMongo object

    Returns:
        a dictionary representation of obj
    """
    dict = {}

    for key in obj.keys():
        if key == '_id':
            dict[key] = str(obj[key])
        else:
            dict[key] = obj[key]

    return dict

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
    """Returns True if postal code is valid, otherwise returns False.

    Args:
        postal_code(str): a postal_code to validate

    Returns:
        True if postal_code is valid, otherwise returns False.
    """
    # TODO: implement this
    return True

def snow_day_proba(postal_code):
    """Returns the percent probability that tomorrow is a snowday (or -1) if tomorrow is not a school day.

    Args:
        postal_code (str): a validated postal code

    Returns:
        (int): the probability that tomorrow is a snowday or -1 if tomorrow is not a school day.
    """
    day_of_week = datetime.datetime.today().weekday() # 0=Monday, ...,6=Sun

    # If day of the week is Fri or Sat, then tomorrow is not a school day
    if day_of_week == 4 or day_of_week == 5:
        return -1
    else:
        return random.randint(0,100)