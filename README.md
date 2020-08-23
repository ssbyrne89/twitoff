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
