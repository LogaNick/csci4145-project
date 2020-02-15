"""This file contains the api for the Student Life News web service"""

# External imports
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson import json_util
from bson.objectid import ObjectId
import datetime

# internal imports
from news import obj_to_dict

# Instatiate app and Flask-MongoDB
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://nicholasbarreyre:zbYKVIASLhvZI3OC@csci4145-5m4ga.azure.mongodb.net/test?retryWrites=true&w=majority"
mongo = PyMongo(app)

# A minimal web server to get started
@app.route('/')
def index():
    return '<h1>You are at the Student Life News API</h1>'

@app.route('/news', methods=['GET', 'POST'])
def get_news():
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
    elif request.method == 'POST':
        # TODO: validate data before post
        assert request.json is not None

        # This return an object of type InsertOneResult
        result = mongo.db.news.insert_one(request.json)

        # TODO: use InsertOneResult properly in this response
        return "Successfully inserted news in DB"
    else:
        # TODO: handle error properly
        return 'ERROR: invalid HTTP request'



@app.route('/news/<_id>', methods=['GET', 'DELETE'])
def get_news_by_id(_id):
    """Get a news objects by its ID in JSON format (GET) or deletes a news object by its ID (DELETE).

    Args:
        _id (PyMongo built in id): the key for the desired news object

    Returns:
        a jsonified version of the News object
    """

    if request.method == 'GET':
        news_obj = mongo.db.news.find_one({'_id': ObjectId(_id)})
        news_json = jsonify(obj_to_dict(news_obj))

        return news_json
    elif request.method == 'DELETE':
        # The following query returns an object of type DeleteResult
        _ = mongo.db.news.delete_one({'_id': ObjectId(_id)})

        # TODO: use the DeleteResult properly when creating response
        return "Delete successful"
    else:
        #TODO: handle this case properly
        return "Error"


#TODO delete this before deployment
def create_mock_data():
    """Create mock data for development."""

    # Clear DB
    mongo.db.news.delete_many({})

    # Make some fake news
    fake_news = [{'body': "This is some news", 'user':"Nick"}, {'body': "This is some more news", 'user': "Random"}]

    # Insert multiple documents
    mongo.db.news.insert_many(fake_news)

if __name__ == '__main__':
    #TODO: Remove this before deployment
    create_mock_data()

    app.run(debug=True)
