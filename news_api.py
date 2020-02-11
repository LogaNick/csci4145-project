"""This file contains the api for the Student Life News web service"""

from flask import Flask
import pymongo
import news
app = Flask(__name__)

# A minimal web server to get started
@app.route('/')
def index():
    return 'You are at the Student Life News API'

@app.route('/news')
def news():
    """Returns a collection of news objects in JSON format.

    Returning a Python dictionary with Flask will suffice since
    dictionaries are automatically converted to JSON.
    """
    news_objects = news.get_news()
    return news_objects

def create_mock_data():
    """Create mock data for development."""
    #TODO delete this before deployment
    pass

def connect_db():
    """Connect to MongoDB

    Returns:
        pymongo.MongoClient instance
    """
    client = pymongo.MongoClient(
        "mongodb+srv://nicholasbarreyre:zbYKVIASLhvZI3OC@csci4145-5m4ga.azure.mongodb.net/test?retryWrites=true&w=majority")
    db = client.csci4145
    return db

if __name__ == '__main__':
    db = connect_db()

    #TODO: Remove this before deployment
    create_mock_data()

    app.run()
