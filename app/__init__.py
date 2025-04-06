from flask import Flask
from app.database import init_db
from app.routes import spartan_routes


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    init_db(app)  # Initialize DB connection
    app.register_blueprint(spartan_routes)  # Register routes

    return app
