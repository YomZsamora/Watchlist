from flask import render_template
from . import main # import the app instance

@main.app_errorhandler(404) # Since we are defining our error handler inside our blueprint we import the blueprint instance main and use it to define our decorator.
def four_Ow_four(error):
    '''
    Function to render the 404 error page
    '''
    return render_template('fourOwfour.html'), 404 # Look for fourOwfour.html file in templates and render that when we get 404 error