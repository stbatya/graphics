"""App initialisation module"""

import os
import pandas as pd
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app(test_config=None):
    """App factory"""
    app = Flask(__name__, instance_relative_config=True)

    #App configuration.
    app.config.from_mapping(
        SECRET_KEY='Kirill',
        SQLALCHEMY_DATABASE_URI = "mysql://"
        "{username}:{password}@{hostname}/{databasename}".format(
        username="Farwander",
        password="admin1234",
        hostname="Farwander.mysql.pythonanywhere-services.com",
        databasename="Farwander$graph_app",
        )
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)


    from .models import Insurance


    #Ensure the instance folder exists.
    #Current version doesn't use this actually.
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #Register database.
    db.init_app(app)

    #import all blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .graphics import graphics as graphics_blueprint
    app.register_blueprint(graphics_blueprint)

    return app
