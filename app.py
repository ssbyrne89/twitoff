from flask import Flask

# example of a factory pattern
def create_app():
    """create and configure an instance of the FLask application"""
    app = Flask(__name__)

    # ... TODO make the app
    @app.route('/')
    def root():
        return "Hello,Twitoff!"

    return app
