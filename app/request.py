from app import app # import the app instance
import urllib.request, json # import the Python urllib.request module that will help us create a connection to our API URL

api_key = app.config['MOVIE_API_KEY'] # Getting api key
base_url = app.config['MOVIE_BASE_URL'] # Getting the movie base url

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
