import unittest
import pandas as pd
from movies import movie_csv, movies_by_year_lookup


# Test concept used for first function in movies.py
class TestMovieLookup(unittest.TestCase):
    def setUp(self):
        self.movie_csv = movie_csv
        self.movie_csv_lower = self.movie_csv['Title'].str.lower().values

        self.in_title = 'The Artist'.lower()
        self.not_title_in = 'Thor'.lower()
        self.mixed_title_in = 'ThE ArTiSt'.lower()
        self.mixed_tile_not_in = 'ThOr'.lower()

        self.not_found = 'Movie is not in the dataframe'
        self.found = 'Movie is in the dataframe'
        
    # Test if known movie in proper case is in dataframe
    def test_title_in(self):
        self.assertIn(self.in_title,self.movie_csv_lower,msg=self.not_found)

     # test if known not-present movie is not in the dataframe
    def test_title_not_in(self):
        self.assertNotIn(self.not_title_in,self.movie_csv_lower,msg=self.found)

     #test if known movie entered in mixed case is in the dataframe
    def test_mixed_title_in(self):
        self.assertIn(self.mixed_title_in,self.movie_csv_lower,msg=self.not_found)

    #test if known not-present movie entered in mixed case is not in the dataframe
    def test_mixed_title_not_in(self):
        self.assertNotIn(self.mixed_tile_not_in,self.movie_csv_lower,msg=self.found)        

if __name__ == '__main__':
    unittest.main()