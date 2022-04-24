from app import app # import the app instance
import urllib.request, json # import the Python urllib.request module that will help us create a connection to our API URL
from .models import movie # import movie from our models package
Movie = movie.Movie

api_key = app.config['MOVIE_API_KEY'] # Getting api key
base_url = app.config['MOVIE_API_BASE_URL'] # Getting the movie base url

def get_movies(category):
    '''
    Function that gets the json response to our url request
    '''
    get_movies_url = base_url.format(category, api_key) # We use the .format() method on the base_url and pass in the movie category and the api_key. 

    # We then use with as our context manager to send a request using theurllib.request.urlopen() function that takes in the get_movies_url as an argument and sends a request as url
    with urllib.request.urlopen(get_movies_url) as url:
        get_movies_data = url.read() # We use the read() function to read the response and store it in a get_movies_datavariable.
        get_movies_response = json.loads(get_movies_data) # convert the JSON response to a Python dictionary using json.loads function

        movies_result = None # 

        if get_movies_response['results']:
            movie_results_list = get_movies_response['results']
            movies_result = process_results(movie_results_list) #  process_results() function that takes in the list of dictionary objects and returns a list of movie objects 

    return movies_result


def process_results(movie_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    movie_results = [] # create an empty list movie_results this is where we will store our newly created movie objects.

    for movie_item in movie_list: # loop through the list of dictionaries
        # using the get() method and pass in the keys so that we can access the values.
        id = movie_item.get('id')
        title = movie_item.get('title')
        overview = movie_item.get('overview')
        poster = movie_item.get('poster_path')
        vote_average = movie_item.get('vote_average')
        vote_count = movie_item.get('vote_count')

        if poster: # check if the movie_item has a poster
            movie_object = Movie(id, title, overview, poster, vote_average, vote_count) # create the movie object. 
            movie_results.append(movie_object) # append created object to our empty list.
    
    return movie_results # return the list with movie objects.

def get_movie(id):
    get_movie_details_url =  base_url.format(id, api_key) # # We use the .format() method on the base_url and pass in the movie id and the api_key. 

    with urllib.request.urlopen(get_movie_details_url) as url:
        movie_details_data = url.read()
        movie_details_response = json.loads(movie_details_data)

        movie_object = None

        if movie_details_response:
            # using the get() method and pass in the keys so that we can access the values.
            id = movie_details_response.get('id')
            title = movie_details_response.get('original_title')
            overview = movie_details_response.get('overview')
            poster = movie_details_response.get('poster_path')
            vote_average = movie_details_response.get('vote_average')
            vote_count = movie_details_response.get('vote_count')

            movie_object = Movie(id, title, overview, poster, vote_average, vote_count) # Creates the movie object

        return movie_object

def search_movie(movie_name):
    search_movie_url = 'https://api.themoviedb.org/3/search/movie?api_key={}&query={}'.format(api_key, movie_name) # new URL for our search request

    with urllib.request.urlopen(search_movie_url) as url:
        search_movie_data = url.read()
        search_movie_response = json.loads(search_movie_data)

        search_movie_results = None

        if search_movie_response['results']:
            search_movie_list = search_movie_response['results']
            search_movie_results = process_results(search_movie_list)

        return search_movie_results

