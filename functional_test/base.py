from selenium import  webdriver
from unittest import TestCase

class FunctionalTest(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.live_url = 'http://localhost:1337'