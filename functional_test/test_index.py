
# Create your tests here.
from functional_test.base import FunctionalTest


class TestIndex(FunctionalTest):

    def test_index(self):
        self.driver.get(self.live_url)

        self.assertIn(self.driver.title, "Movie Shop")