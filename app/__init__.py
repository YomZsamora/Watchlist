from flask import Flask # import the Flask class from flask module
from .config import DevConfig
from flask_bootstrap import Bootstrap

app = Flask(__name__, instance_relative_config = True) # Initializing application. instance_relative_config which allow us to connect to the instance/folder

app.config.from_object(DevConfig) # Setting up configuration
app.config.from_pyfile('config.py') # connects to the config.py file and all its contents are appended to the app.config

bootstrap = Bootstrap(app) # Initializing Bootstrap Extensions

from app import views # import our views file from the app folder. This will allow us to create views.
