"""SQLAlchemy models and utility functions for Twitoff.
this connects to the db and SQLAlchemy runs sql through sequalized js"""
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()  # instantiate the class, works the same for sqlite & postgres

class User(DB.Model):
    """Twitter users corresponding to Tweets"""
    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.String(15), nullable=False)
    newest_tweet_id = DB.Column(DB.BigInteger)
    
# the line below is called a representation method; it's an inner method to make a nice output
# instead of a memory address
    def __repr__(self):
        return '-User {}-'.format(self.name)


class Tweet(DB.Model):
    """Tweet text and data"""
    id = DB.Column(DB.BigInteger, primary_key=True)
    text = DB.Column(DB.Unicode(300)) #Allows for text + links, ALSO make sure to use UNICODE b/c emojis and such
    embedding = DB.Column(DB.PickleType)
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey('user.id'), nullable=False)
    user = DB.relationship('User', backref=DB.backref('tweets', lazy=True))

# the backref helps you populate the tweets w/o doing an explicit join
    def __repr__(self):
        return '-Tweet {}-'.format(self.text)
