from selenium import  webdriver
import unittest
# Create your tests here.
from functional_test.base import FunctionalTest


class TestIndex(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.live_url = 'http://localhost:8000'

    def test_index(self):
        self.driver.get(self.live_url)

        self.assertIn(self.driver.title, "MovieID")