import eventlet
eventlet.monkey_patch()
from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config[
        'SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['DEBUG'] = True
    app.config['FLASK_ENV'] = 'development'

    @app.route('/')
    def hello_world():
        from post import Post
        Post.query.all()
        return 'Hello World!'

    db.init_app(app)
    print('APP INITED')
    return app
