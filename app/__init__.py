"""A simple flask web app"""
import logging
import os
from logging.handlers import RotatingFileHandler

import flask_login
from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_wtf.csrf import CSRFProtect

from app.cli import create_database
from app.context_processors import utility_text_processors
from app.db import db
from app.db.models import User
from app.error_handlers import error_handlers
from app.logging_config import log_con, LOGGING_CONFIG
from app.db import database
from flask_cors import CORS
login_manager = flask_login.LoginManager()


def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    if  os.environ.get("FLASK_ENV") == "production":
        app.config.from_object("app.config.ProductionConfig")
    elif os.environ.get("FLASK_ENV") == "development":
        app.config.from_object("app.config.DevelopmentConfig")
    elif os.environ.get("FLASK_ENV") == "testing":
        app.config.from_object("app.config.TestingConfig")

    # https://bootstrap-flask.readthedocs.io/en/stable/
    bootstrap = Bootstrap5(app)
    app.register_blueprint(database)
    # these load functionality without a web interface
    app.register_blueprint(log_con)
    app.register_blueprint(error_handlers)
    app.context_processor(utility_text_processors)
    # add command function to cli commands
    app.cli.add_command(create_database)
    db.init_app(app)
    api_v1_cors_config = {
    "methods": ["OPTIONS", "GET", "POST"],
    }
    CORS(app, resources={"/api/*": api_v1_cors_config})
    # Run once at startup:
    @app.route('/')
    def hello():
        return 'Hello, World!'

    return app
