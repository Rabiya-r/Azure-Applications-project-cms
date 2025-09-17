"""
The flask application package.
"""

import logging
from logging.handlers import RotatingFileHandler
import os
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

app = Flask(__name__)
app.config.from_object(Config)

# ---------------- Logging Setup ----------------
if not os.path.exists('logs'):
    os.mkdir('logs')

file_handler = RotatingFileHandler('logs/cms_app.log', maxBytes=10240, backupCount=10)
file_handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
))
file_handler.setLevel(logging.INFO)
app.logger.addHandler(file_handler)

# Set overall app logger level
app.logger.setLevel(logging.INFO)
app.logger.info('CMS Flask App startup')

# ---------------- Flask Extensions ----------------
Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

# Import views after app is created
import FlaskWebProject.views

