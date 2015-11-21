from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.httpauth import HTTPBasicAuth
from flask.ext.restful import Api


db = SQLAlchemy()
auth = HTTPBasicAuth()


def register_apis(app):
    from .views import (Register, Login, Profile)
    api = Api(app)
    api.add_resource(Register, '/v1/register', endpoint='register')
    api.add_resource(Login, '/v1/login', endpoint='login')
    api.add_resource(Profile, '/v1/profile', endpoint='profile')


def create_app():
    app = Flask(__name__)
    db.init_app(app)

    register_apis(app)

    app.config.from_object(config)
    return app

from app import views
