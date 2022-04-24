from flask import render_template
from app import app # import the app instance

@app.errorhandler(404) # passes in the error we receive.
def four_Ow_four(error):
    '''
    Function to render the 404 error page
    '''
    return render_template('fourOwfour.html'), 404 # Look for fourOwfour.html file in templates and render that when we get 404 error