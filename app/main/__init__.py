from flask import Blueprint
main = Blueprint('main',__name__) # We  initialize the Blueprint class by creating a variable main.
from . import views,errors