import os
from flask import Flask
#from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
#from flaskr import db

"""app initialisation module"""

db = SQLAlchemy()

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='Kirill',
        SQLALCHEMY_DATABASE_URI=''
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
#   login_manager = LoginManager()
#    login_manager.login_view = 'auth.login'
#    login_manager.init_app(app)

    from .models import User

#    @login_manager.user_loader
#    def load_user(user_id):
#        return User.query.get(int(user_id))


    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .graphics import graphics as graphics_blueprint
    app.register_blueprint(graphics_blueprint)
    
    return app
