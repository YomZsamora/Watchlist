import unittest
from app.models import Movie


class MovieTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_movie = Movie(1234, 'Python Must Be Crazy', 'A thrilling new Python Series', 'https://image.tmdb.org/t/p/w500/khsjha27hbs', 8.5, 129993)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_movie, Movie)) # checks if the object self.new_movie is an instance of the Movie class.

