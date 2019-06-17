import os
import tempfile

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

bootstrap = Bootstrap()
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'asdjalsdkjlsadjlsakjdoo'
    bootstrap.init_app(app)
    app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:////' + os.path.join(tempfile.gettempdir(), 'quiz.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
