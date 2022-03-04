import unittest
import pandas as pd


class TestMovieLookup(unittest.TestCase):
    def setUp(self):
        self.movie_csv = pd.read_csv('MovieBoardsDigital.csv', usecols=['Title'])
        self.movie_list = self.movie_csv['Title'].str.lower().tolist()
    
    def test_title_in(self):
        self.assertIn('The Artist'.lower(),self.movie_list,msg='Movie is not in the dataframe')

    def test_title_not_in(self):
        self.assertNotIn('Thor'.lower(),self.movie_list,msg='Movie is in the dataframe')

    def test_title_lower(self):
        self.assertIn('THE ARTIST'.lower(),self.movie_list,msg='Movie is not in the dataframe')

    def test_nonexistent_title_lower(self):
        self.assertNotIn('THOR',self.movie_list,msg='Movie is not in the dataframe')


if __name__ == '__main__':
    unittest.main()