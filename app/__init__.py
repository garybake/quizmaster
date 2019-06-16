import os
import tempfile

from flask import Flask
from flask_bootstrap import Bootstrap
# from flask_mail import Mail
# from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
# from config import config
# from flask_api import FlaskAPI

basedir = os.path.abspath(os.path.dirname(__file__))

bootstrap = Bootstrap()
# mail = Mail()
# moment = Moment()
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    # app.config.from_object(config[config_name])
    # config[config_name].init_app(app)
    app.config['SECRET_KEY'] = 'asdjalsdkjlsadjlsakjdoo'
    bootstrap.init_app(app)
    # mail.init_app(app)
    # moment.init_app(app)
    # app.config['SQLALCHEMY_DATABASE_URI']
    app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:////' + os.path.join(tempfile.gettempdir(), 'quiz.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # db.create_all()

    # attach routes and custom pages here
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
