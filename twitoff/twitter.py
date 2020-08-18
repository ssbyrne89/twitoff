"""Retrieve Tweets, embeddings, and persist in the database."""
from os import getenv
import basilica
import tweepy
from .models import db, Tweet, User


TWITTER_USERS = ['calebhicks', 'elonmusk', 'rrherr', 'SteveMartinToGo',
                 'alyankovic', 'nasa', 'sadserver', 'jkhowland', 'austen',
                 'common_squirrel', 'KenJennings', 'conanobrien',
                 'big_ben_clock', 'IAM_SHAKESPEARE']

# TODO don't have raw secrets in the code, move to .env!
TWITTER_API_KEY = getenv('TWITTER_API_KEY')
TWITTER_API_SECRET_KEY = getenv('TWITTER_API_SECRET_KEY')
TWITTER_AUTH = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET_KEY)
TWITTER = tweepy.API(TWITTER_AUTH)
BASILICA = basilica.Connection(getenv('BASILICA_KEY'))

def add_or_update_user(username):
    """Add or update a user and their Tweets, error if not a Twitter user."""
    try:
        twitter_user = TWITTER.get_user(username)
        db_user = (User.query.get(twitter_user.id) or
                User(id=twitter_user.id, name=username))
        db.session.add(db_user)
        # Lets get the tweets - focusing on primary (not retweet/reply)
        tweets = twitter_user.timeline(
            count=200, exclude_replies=True, include_rts=False,
            tweet_mode='extended', since_id=db_user.newest_tweet_id
        )
        if tweets:
            db_user.newest_tweet_id = tweets[0].id
        for tweet in tweets:
            embedding = BASILICA.embed_sentence(tweet.full_text,
                                                model='twitter')
            db_tweet = Tweet(id=tweet.id, text=tweet.full_text[:300], embedding=embedding)
            db_user.tweets.append(db_tweet)
            db.session.add(db_tweet)
        db.session.commit()
    except Exception as e:
        print('Error processing {}: {}'.format(username, e))
        raise e
    else:
        db.session.commit()

def insert_example_users():
    """Example data to play with."""
    austen =User(id=1, name='austen')
    elon = User(id=2, name='elonmusk')
    db.session.add(austen)
    db.session.add(elon)
    db.session.commit()

"""



"""