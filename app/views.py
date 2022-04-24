from flask import render_template # import the render_template() that takes in the name of a template file as the first argument.
from app import app # import the app instance from the app folder.
from .request import get_movies #  import the get_movies() function from the request module.

@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    popular_movies = get_movies('popular') # Call our get_movies() function and pass in "popular" as an argument. 
    upcoming_movies = get_movies('upcoming') # Call our get_movies() function and pass in "upcoming" as an argument. 
    now_showing_movies = get_movies('now_playing') # Call our get_movies() function and pass in "now_playing" as an argument. 
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html', title = title, popular = popular_movies, upcoming = upcoming_movies, now_showing = now_showing_movies) # searches for the template file in our app/templates/ sub directory and loads it.

@app.route('/movie/<movie_id>') # Angle brackets <> is dynamic. And any route mapped to this will be passed.
def movie(movie_id):
    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('movie.html', id = movie_id)