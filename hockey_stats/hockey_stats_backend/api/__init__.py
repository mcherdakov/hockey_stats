from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

from hockey_stats_backend.api.config import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app(app_name='hockey_stats'):
    app = Flask(app_name)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    cors = CORS(app, resources={r'/api/*': {'origins': '*'}})

    from hockey_stats_backend.api.api import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app
