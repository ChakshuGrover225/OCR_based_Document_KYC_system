from flask import Flask

# Rename the Flask app object to avoid conflict with folder name
flask_app = Flask(__name__)

# Load configuration
flask_app.config.from_object('app.config')

# Import routes so endpoints are registered
from app import routes
