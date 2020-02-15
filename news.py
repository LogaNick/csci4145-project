"""This file implements the helper functions for news and comment data."""
import datetime
from flask import jsonify


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
