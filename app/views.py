from flask import render_template, request, redirect, url_for # import the render_template() that takes in the name of a template file as the first argument.
from app import app # import the app instance from the app folder.
from .request import get_movies, get_movie, search_movie #  import the get_movies(), get_movie() & search_movie() functions from the request module.

@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    popular_movies = get_movies('popular') # Call our get_movies() function and pass in "popular" as an argument. 
    upcoming_movies = get_movies('upcoming') # Call our get_movies() function and pass in "upcoming" as an argument. 
    now_showing_movies = get_movies('now_playing') # Call our get_movies() function and pass in "now_playing" as an argument. 

    title = 'Home - Welcome to The best Movie Review Website Online'

    search_movie = request.args.get('movie_query') # We pass in the name of the query and the value is returned.

    if search_movie:
        return redirect(url_for('search', movie_name = search_movie)) # redirect function that redirects us to another view function.

    return render_template('index.html', title = title, popular = popular_movies, upcoming = upcoming_movies, now_showing = now_showing_movies) # searches for the template file in our app/templates/ sub directory and loads it.

@app.route('/movie/<int:id>') # Angle brackets <> is dynamic. And any route mapped to this will be passed.
def movie(id):
    '''
    View movie page function that returns the movie details page and its data
    '''
    movie = get_movie(id) # Call our get_movies() function and pass in a movie id as an argument. 
    title = f'{movie.title}' # Use movie's title as page title.
    return render_template('movie.html', title = title, movie = movie)

@app.route('/search/<movie_name>')
def search(movie_name):
    '''
    View function to display the search results
    '''
    movie_name_list = movie_name.split(' ')
    movie_name_format = "+".join(movie_name_list)
    searched_movies = search_movie(movie_name_format)
    title = f'search results for {movie_name}'
    return render_template('search.html', title=title, movies=searched_movies)