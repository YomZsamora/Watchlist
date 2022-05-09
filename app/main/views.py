from flask import render_template, request, redirect, url_for # import the render_template() that takes in the name of a template file as the first argument.
from . import main # import the app instance from the app folder.
from ..request import get_movies, get_movie, search_movie #  import the get_movies(), get_movie() & search_movie() functions from the request module.

from ..models import Reviews # Import the Review class from our models folder.
from .forms import ReviewForm # import the ReviewForm class from our forms file.


@main.route('/')
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
        # redirect function that redirects us to another view function.
        return redirect(url_for('search', movie_name = search_movie))  # url_for function that passes in the search view function together with the dynamic movie_name
    
    return render_template('index.html', title = title, popular = popular_movies, upcoming = upcoming_movies, now_showing = now_showing_movies) # searches for a template file in our app/templates/ sub directory and loads it.

@main.route('/movie/<int:id>') # Angle brackets <> is dynamic. And any route mapped to this will be passed.
def movie(id):
    '''
    View movie page function that returns the movie details page and its data
    '''
    movie = get_movie(id) # Call our get_movies() function and pass in a movie id as an argument. 
    title = f'{movie.title}' # Use movie's title as page title.
    reviews = Reviews.get_reviews(movie.id)
    return render_template('movie.html', title = title, movie = movie, reviews = reviews)

@main.route('/search/<movie_name>')
def search(movie_name):
    '''
    View function to display the search results
    '''
    movie_name_list = movie_name.split(' ')
    movie_name_format = "+".join(movie_name_list)
    searched_movies = search_movie(movie_name_format)
    title = f'search results for {movie_name}'
    return render_template('search.html', title=title, movies=searched_movies)

@main.route('/movie/review/new/<int:id>', methods = ['GET','POST'])
def new_review(id):
    form = ReviewForm() # create an instance of the ReviewForm class
    movie = get_movie(id) # call the get_movie and pass in the ID to get the movie object for the movie with that ID.

    if form.validate_on_submit(): # validate_on_submit() method returns True when the form is submitted and all the data has been verified by the validators.
        title = form.title.data
        review = form.review.data
    
        new_review = Reviews(movie.id, title, movie.poster, review)
        new_review.save_review()
        return redirect(url_for('movie', id=movie.id))

    title = f'{movie.title} review'
    return render_template('new_review.html',title = title, review_form=form, movie=movie)
