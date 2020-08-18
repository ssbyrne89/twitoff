"""
Minimal example Flask web application
"""


from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


"""
To see it in the browser,
create a connection to the server via
the CLI. In the CLI, w/in the file
directory type:
export FLASK_APP=hello.py
press ENTER
then type:
flask run
"""
