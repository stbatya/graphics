import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pandas as pd

"""app initialisation module"""

db = SQLAlchemy()

#app factory
def create_app(test_config=None):
    #define app
    app = Flask(__name__, instance_relative_config=True)
    #app configuration
    app.config.from_mapping(
        SECRET_KEY='Kirill',
        SQLALCHEMY_DATABASE_URI = "mysql://{username}:{password}@{hostname}/{databasename}".format(
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


    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #register database
    db.init_app(app)

    #import all blueprints

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .graphics import graphics as graphics_blueprint
    app.register_blueprint(graphics_blueprint)

    return app
