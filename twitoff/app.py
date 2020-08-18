"""Main app/routing file for TwitOff."""
from flask import Flask, render_template
from .models import db, User
from .twitter import insert_example_users
from os import getenv

# example of a factory pattern
def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    # ... TODO make the app!
    @app.route('/')
    def root():
        return render_template('base.html', title='Home',
                               users=User.query.all())

    @app.route('/update')
    def update():
        # Reset the database
        insert_example_users()
        return render_template('base.html', title='Users updated!',
                               users=User.query.all())

    @app.route('/reset')
    def reset():
        db.drop_all()
        db.create_all()
        return render_template('base.html', title='Reset database!')

    return app
