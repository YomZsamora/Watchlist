from flask import render_template # import the render_template() that takes in the name of a template file as the first argument.
from app import app # import the app instance from the app folder.

@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html', title = title) # searches for the template file in our app/templates/ sub directory and loads it.

@app.route('/movie/<movie_id>') # Angle brackets <> is dynamic. And any route mapped to this will be passed.
def movie(movie_id):
    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('movie.html', id = movie_id)