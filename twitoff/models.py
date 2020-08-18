"""SQLAlchemy models and utility functions for Twitoff.
this connects to the db and SQLAlchemy runs sql through sequalized js"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # instantiate the class, works the same for sqlite & postgres

class User(db.Model):
    """Twitter users corresponding to Tweets"""
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(15), nullable=False)
    newest_tweet_id = db.Column(db.BigInteger)
    
# the line below is called a representation method; it's an inner method to make a nice output
# instead of a memory address
    def __repr__(self):
        return '-User {}-'.format(self.name)


class Tweet(db.Model):
    """Tweet text and data"""
    id = db.Column(db.BigInteger, primary_key=True)
    text = db.Column(db.Unicode(300)) #Allows for text + links, ALSO make sure to use UNICODE b/c emojis and such
    embedding = db.Column(db.PickleType)
    user_id = db.Column(db.BigInteger, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('tweets', lazy=True))
# the backref helps you populate the tweets w/o doing an explicit join
    def __repr__(self):
        return '-Tweet {}-'.format(self.text)
