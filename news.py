"""This file implements the News class."""
import datetime
from flask import jsonify

class News():
    def __init__(self, username, time, body, comments=None):
        """Instantiate a news object

        Args:
            username (string): the username of the person posting this news
            time (datetime.Datetime): the time that the news was inserted in the DB
            body (string): the body of the news -- the news itself
            comments (list of Comment objects, optional): the comments associated with this news object. Defaults to
            None.
        """
        self.username = username
        self.time = time
        self.body = body
        self.comments = comments #TODO(@nicholasbarreyre) validate this

    def edit_body(self, new_body):
        self.body = new_body

    def add_comment(self, comment):
        pass

    def remove_comment(self, index):
        pass

    @staticmethod
    def get_news():
        """Returns all news objects from DB."""
        pass

    @staticmethod
    def obj_to_dict(news_obj):
        json = {}

        for key in news_obj.keys():
            if key == '_id':
                json[key] = str(news_obj[key])
            else:
                json[key] = news_obj[key]

        return json

class Comment():
    def __init__(self, body, time):
        """Instatiate a comment object.

        Args:
            body (string): the content of the comment
            time (datetime.Datetime): the time the comment was made
        """
        self.body = body #TODO(nicholasbarreyre) validate this
        self.time = time

    def edit_body(self, new_body):
        self.body = new_body
