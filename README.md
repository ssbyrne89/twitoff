# twitoff
Flask web app for comparing twitter accounts

to open a connection, open up a CLI and type:
export FLASK_APP=twitoff
press enter
then type:
flask run
press enter

the CLI now becomes occupied and displays a live log of requests and responses

to run on HEROKU:
you need a Procfile in the directory for the web app to work and set the timeout to -t 120 


difference b/t git and github, git tracks changes and github stores. git is the software and github is the hub to store data.


deploying to heroku is not much different than pushing to github. heroku uses git for deploying but then actually runs the code you push to deploy the web app


to check if you're already logged in to heroku CLI first type: pipenv shell
then type: heroku authorizations
for more commands w/ heroku type: heroku --help

be sure to have "from os import getenv" in your app.py so you can set the environment and connect to DB via .env



ALSO in order to deploy to heroku you need to have a Procfile in the top of the repository next to the Pipfile and .env  Procfile is short for 'process,'
and this where we give instructions and tell heroku how to run the app. 

Heroku's term for server is dyno or dino and in the Procfile write:
web: gunicorn twitoff:APP -t 120
the line above basically says: the web dyno is gunicorn and it should run the twitoff APP but give it a very generous timeout b/c adding users can take some time

PACKAGES OVERVIEW:
Pipfile
[[source]]
name = "pypi"
url = "https://pypi.org/simple"
verify_ssl = true

[dev-packages]
pylint = "*"

[packages]
flask = "*"  --the backend routing
jinja2 = "*"  --nice frontend templates, for looks
flask-sqlalchemy = "*"  -- SQLAlchemy: the DB connection, the object relational mapper(ORM), does SQL
tweepy = "*"  --external connection APIs, getting stuff
basilica = "*"  --external connection APIs, getting stuff from other APIs
python-dotenv = "*" loading our settings, to have PWs available for heroku but still undisclosed in github, this is where you set the environment variables
scikit-learn = "*"  -- the datascience, the model for running analysis
psycopg2-binary = "*"  --needed for heroku deployment
gunicorn = "*"  --production webserver, once deployed on heroku gunicorn is the server

[requires]
python_version = "3.7"