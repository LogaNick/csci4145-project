"""This file contains the api for the Student Life News web service"""

# External imports
from flask import Flask, jsonify, request, abort
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import requests
from datetime import datetime, date, timedelta

# internal imports
from utils import *
from constants import *

# Instatiate app and Flask-MongoDB
app = Flask(__name__)
app.config["MONGO_URI"] = MONGO_URI
mongo = PyMongo(app)

# A minimal web server to get started
@app.route('/')
def index():
    return '<h1>You are at the Student Life News API</h1>'

@app.route('/weather/<date_string>', methods=['GET'])
#TODO: allow user location input
def get_weather(date_string):
    """Returns a json with weather data about a given day in Halifax
    Args:
        date_string (str): a date in YYYY-MM-DD format
    """
    try:
        d = datetime.date(*(int(s) for s in date_string.split('-')))
    except:
        abort(400, 'The specified date format was incorrect (should be YYYY-MM-DD).')
    
    date_difference = d-datetime.date.today()
    if (date_difference > timedelta(days = 16)) or (date_difference < timedelta(days = -1)):
        abort(400, 'The specified date format was outside of the 16 day range.')

    # Formatting required by weather API, using noon (Halifax time)
    date_string = date_string+'T12:00:00-0400'

    # Make weather API request
    weather_result = weather_req(date_string)

    return weather_result.json()

@app.route('/news', methods=['GET', 'POST'])
def news():
    """Returns a collection of news objects in JSON format (GET) or POST a piece of news.

    Returning a Python dictionary with Flask will suffice since
    dictionaries are automatically converted to JSON.
    """

    if request.method == 'GET':
        # Get requests to /news means return collection of news objects in DB
        news_objs = []
        for news_obj in mongo.db.news.find():
            news_objs.append(obj_to_dict(news_obj))
        return jsonify(news_objs)

    else:
        #Validation of POST requests
        if request.json is None:
            abort(400, "Error: None type is not acceptable as news.")
        elif type(request.json) == list:
            for item in request.json:
                if len(item) > 3:
                    abort(400, "Too many fields in entry.")
                elif 'body' not in item:
                    abort(400, "Field 'body' not found.")
                elif 'user' not in item:
                    abort(400, "Field 'user' not found.")
                elif 'title' not in item:
                    abort(400, "Field 'title' not found.")
                elif type(item['body']) != str:
                    abort(400, "Error: 'body' of entry is not a valid type.")
                elif type(item['user']) != str:
                    abort(400, "Error: 'user' of entry is not of valid type.")
                elif type(item['title']) != str:
                    abort(400, "Error: 'title' of entry is not of valid type.")
                item['comments'] = []
                item['date'] = datetime.datetime.now()
            result = mongo.db.news.insert_many(request.json)
        else:
            if len(request.json) > 3:
                abort(400, "Too many fields in entry.")
            elif 'body' not in request.json:
                abort(400, "Field 'body' not found.")
            elif 'user' not in request.json:
                abort(400, "Field 'user' not found.")
            elif 'title' not in request.json:
                abort(400, "Field 'title' not found.")
            elif type(request.json['body']) != str:
                abort(400, "Error: 'body' of entry is not a valid type.") 
            elif type(request.json['user']) != str:
                abort(400, "Error: 'user' of entry is not of valid type.")
            elif type(request.json['title']) != str:
                abort(400, "Error: 'title' of entry is not of valid type.")
            else:
                request.json['comments'] = []
                request.json['date'] = datetime.datetime.now()
                result = mongo.db.news.insert_one(request.json)

        # TODO: use InsertOneResult properly in this response
        return "Successfully inserted news in DB"

@app.route('/news/<_id>', methods=['GET', 'DELETE', 'PUT'])
def news_by_id(_id):
    """Get a news objects by its ID in JSON format (GET) or deletes a news object by its ID (DELETE).

    Args:
        _id (PyMongo built in id): the key for the desired news object

    Returns:
        a jsonified version of the News object
    """
    # TODO: handle case when no news objct with that id
    if request.method == 'GET':
        try:
            news_obj = mongo.db.news.find_one({'_id': ObjectId(_id)})
            news_json = jsonify(obj_to_dict(news_obj))
        except:
            return abort(404, "No news exists with the given id.")

        return news_json
    elif request.method == 'DELETE':
        try:
            # The following query returns an object of type DeleteResult
            _ = mongo.db.news.delete_one({'_id': ObjectId(_id)})
            # TODO: use the DeleteResult properly when creating response
            return "Delete successful"
        except:
            return abort(404, "No news exists with the given id.")
    else:
        try:
            if len(request.json) > 2:
                abort(400, "Too many fields in entry.")
            elif request.json is None:
                abort(400, "Error: None type is not an acceptable comment.")
            elif 'user' not in request.json:
                abort(400, "Error: Field 'user' not found.")
            elif 'body' not in request.json:
                abort(400, "Error: Field 'body' not found.")
            elif type(request.json['user']) != str:
                abort(400, "Error: 'user' of entry is not of valid type.")
            elif type(request.json['body']) != str:
                abort(400, "Error: 'body' of entry is not of valid type.")
            else:
                news_obj = mongo.db.news.find_one({'_id': ObjectId(_id)})
                news_json = jsonify(obj_to_dict(news_obj))
                request.json['date'] = datetime.datetime.now()
                temp_news = news_json.get_json()
                temp_news['comments'].append(request.json)
                result = mongo.db.news.update_one({"_id": ObjectId(_id)}, {"$set":{'comments':temp_news['comments']}})
                return "Comment Successful"
        except:
            return abort(404, "No news exists with the given id.")

@app.route('/snowday/<postal_code>', methods=['GET'])
def snowday(postal_code):
    """Returns an integer: the percent probability that tomorrow will be a snow day.

    If tomorrow is a school day, then returns the percent probability that tomorrow will be a snow day. If tomorrow is
    not a school day, then returns -1.

    Args:
        postal_code (str): a valid postal code
    """
    if not is_valid_postal(postal_code.upper()):
        abort(400, "Postal Code is not valid.")

    proba = snow_day_proba(postal_code)

    return jsonify(proba)

def clear_data():
    # Clear DB
    mongo.db.news.delete_many({})

if __name__ == '__main__':
    app.run(debug=True)
