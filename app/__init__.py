from flask import Flask # import the Flask class from flask module
from config import config_options
from flask_bootstrap import Bootstrap 

bootstrap = Bootstrap()

def create_app(config_name):

    app = Flask(__name__) # Initializing application. instance_relative_config which allow us to connect to the instance/folder

    app.config.from_object(config_options[config_name]) # Setting up configuration

    bootstrap.init_app(app) # Initializing Bootstrap Extensions
    
    # Registering the blueprint
    from .main import main as main_blueprint #  import the Blueprint instance
    app.register_blueprint(main_blueprint) # call the register_blueprint() method on the application instance and pass in the blueprint.
    
    # setting config
    from .request import configure_request # Import the configure_request() function from the request.py file.
    configure_request(app)

    return app 
