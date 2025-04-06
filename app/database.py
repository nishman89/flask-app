# app/database.py
from flask_mysqldb import MySQL
from config import config

mysql = MySQL()

def init_db(app):
    """Initialize the database with app configuration."""
    app.config['MYSQL_HOST'] = config["MYSQL_HOST"]
    app.config['MYSQL_USER'] = config["MYSQL_USER"]
    app.config['MYSQL_PASSWORD'] = config["MYSQL_PASSWORD"]
    app.config['MYSQL_DB'] = config["MYSQL_DB"]
    mysql.init_app(app)
