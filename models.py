from flask_sqlalchemy import flask_sqlalchemy


DB = SQLAlchemy()

class User(DB.Model):
    """Twitter users corresponding to Tweets"""
    id = DB.Column(DB.BigInteger, primay_key=True)
    name = DB.Column(DB.String(15), nullable=False)

    def __repr__(self):
        return '-User {}-'.formay(self.name)