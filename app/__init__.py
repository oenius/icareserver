import os

from flask import Flask, jsonify
#from flask.ext.restful import Api, Resource
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.httpauth import HTTPBasicAuth
from flask.ext.restful import Api
from werkzeug.exceptions import HTTPException


db = SQLAlchemy()
auth = HTTPBasicAuth()


def create_app():
    app = Flask(__name__)
    db.init_app(app)
    api = Api(app, errors = custom_errors)

    app.config.from_object(config)
    return app

from app import views
