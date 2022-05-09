from app import create_app # import the app instance.
from flask_script import Manager,Server # Import the Manager class from flask-script that will initialize our extension and the Server class that help us launch our server.

app = create_app('development') # Call the create_app function and pass in the configuration_options key so as to create the application instance.

manager = Manager(app) # Instantiate the Manager class by passing in the app instance.
manager.add_command('server', Server) # Create a command line argument to tell us how to run our application. 

if __name__ == '__main__':
    manager.run() # runs the Flask instance (app)