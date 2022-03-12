import unittest
import pandas as pd
from movies import movie_csv


# Test concept used for first function in movies.py
class TestMovieLookup(unittest.TestCase):
    def setUp(self):
        self.movie_csv = movie_csv
        self.movie_csv_lower = self.movie_csv['Title'].str.lower().values

        self.in_title = 'The Artist'
        self.not_title_in = 'Thor'
        self.mixed_title_in = 'ThE ArTiSt'
        self.mixed_tile_not_in = 'ThOr'

        self.not_found = 'Movie is not in the dataframe'
        self.found = 'Movie is in the dataframe'
        
    # Test if known movie in proper case is in dataframe
    def test_title_in(self):
        self.assertIn(self.in_title.lower(),self.movie_csv_lower,msg=self.not_found)

     # test if known not-present movie is not in the dataframe
    def test_title_not_in(self):
        self.assertNotIn(self.not_title_in.lower(),self.movie_csv_lower,msg=self.found)

     #test if known movie entered in mixed case is in the dataframe
    def test_mixed_title_in(self):
        self.assertIn(self.mixed_title_in.lower(),self.movie_csv_lower,msg=self.not_found)

    #test if known not-present movie entered in mixed case is not in the dataframe
    def test_mixed_title_not_in(self):
        self.assertNotIn(self.mixed_tile_not_in.lower(),self.movie_csv_lower,msg=self.found)        


if __name__ == '__main__':
    unittest.main()