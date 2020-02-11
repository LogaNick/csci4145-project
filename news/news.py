"""This file implements the News class."""

class News():
    def __init__(self, username, body, comments=None):
        """Instantiate a news object

        Args:
            username (string): the username of the person posting this news
            body (string): the body of the news -- the news itself
            comments (list of Comment objects, optional): the comments associated with this news object. Defaults to
            None.
        """
        self.username = username
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

class Comment():
    def __init__(self, body):
        """Instatiate a comment object.

        Args:
            body (string): the content of the comment
        """
        self.body = body #TODO(nicholasbarreyre) validate this

    def edit_body(self, new_body):
        self.body = new_body
