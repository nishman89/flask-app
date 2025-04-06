import json
import os

# Load config.json
config_path = os.path.join(os.path.dirname(__file__), 'config.json')  # Ensure the path is correct
with open(config_path, "r") as config_file:
    config = json.load(config_file)  # Parse JSON data

# Define Config class
class Config:
    MYSQL_HOST = config["MYSQL_HOST"]
    MYSQL_USER = config["MYSQL_USER"]
    MYSQL_PASSWORD = config["MYSQL_PASSWORD"]
    MYSQL_DB = config["MYSQL_DB"]
