"""This file contains the api for the Student Life News web service"""

from flask import Flask
app = Flask(__name__)

# A minimal web server to get started
@app.route('/')
def hello_world():
    return 'Hello, World!'