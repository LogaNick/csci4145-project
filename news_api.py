"""This file contains the api for the Student Life News web service"""

# External imports
from flask import Flask, jsonify
from flask_pymongo import PyMongo
from bson import json_util
from bson.objectid import ObjectId

# internal imports
from news import News

# Instatiate app and Flask-MongoDB
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://nicholasbarreyre:zbYKVIASLhvZI3OC@csci4145-5m4ga.azure.mongodb.net/test?retryWrites=true&w=majority"
mongo = PyMongo(app)

# A minimal web server to get started
@app.route('/')
def index():
    return 'You are at the Student Life News API'

@app.route('/news', methods=['GET'])
def get_news():
    """Returns a collection of news objects in JSON format.

    Returning a Python dictionary with Flask will suffice since
    dictionaries are automatically converted to JSON.
    """
    news_objs = []
    for news_obj in mongo.db.news.find():
        news_objs.append({'_id': str(news_obj['_id']), 'body': news_obj['body'], 'user': news_obj['user']})

    return jsonify(news_objs)

@app.route('/news/<_id>', methods=['GET'])
def get_news_by_id(_id):
    """Get a news objects by its ID in JSON format.

    """
    # TODO(nicholasbarreyre): document this

    news_obj = mongo.db.news.find_one({'_id': ObjectId(_id)})
    news_json = jsonify(News.obj_to_dict(news_obj))

    return news_json

#TODO delete this before deployment
def create_mock_data():
    """Create mock data for development."""

    # Clear DB
    mongo.db.news.delete_many({})

    # Make fake news objects

    # Make mock data
    fake_news = [{'body': "This is some news", 'user':"Nick"}, {'body': "This is some more news", 'user': "Random"}]

    # Insert multiple documents
    mongo.db.news.insert_many(fake_news)

if __name__ == '__main__':
    #TODO: Remove this before deployment
    create_mock_data()

    app.run(debug=True)
