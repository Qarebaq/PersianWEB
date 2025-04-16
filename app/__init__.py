from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
import os

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    Migrate(app, db)

    from .routes import auth, articles
    app.register_blueprint(auth.bp)
    app.register_blueprint(articles.bp)

    os.makedirs(os.path.join(app.static_folder, 'uploads'), exist_ok=True)

    return app
