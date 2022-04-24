from flask import Flask # import the Flask class from flask module
from .config import DevConfig

app = Flask(__name__) # Initializing application

app.config.from_object(DevConfig) # # Setting up configuration

from app import views # import our views file from the app folder. This will allow us to create views.
