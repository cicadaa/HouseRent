from flask import Flask
from .model import db
from .admin import admin
from flask_login import LoginManager
from .api import init_map

login_manager = LoginManager()


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    app.secret_key = b'\x92yi\xcd\xc7@Qy\xea$\x14\x1a\xd6=\x85.'
    db.init_app(app)
    admin.init_app(app)
    init_map(app)
    login_manager.init_app(app)
    app.config['FLASK_ADMIN_SWATCH'] = 'cosmo'
    return app
