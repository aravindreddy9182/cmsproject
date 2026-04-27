"""
The flask application package.
"""

import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

app = Flask(__name__)

app.config.from_object(Config)

# Logging configuration (important for Azure logs)
logging.basicConfig(level=logging.INFO)

if not app.debug:
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s'
    )
    stream_handler.setFormatter(formatter)
    app.logger.addHandler(stream_handler)

app.logger.setLevel(logging.INFO)
app.logger.info('Flask application startup')

# Flask session
Session(app)

# Database
db = SQLAlchemy(app)

# Login manager
login = LoginManager(app)
login.login_view = 'login'
login.login_message = "Please login to access this page."

# Import routes
import FlaskWebProject.views