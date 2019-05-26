from django.test import TestCase
from catalog.models import Movie

# Create your tests here.
class IndexTest(TestCase):

    def setUp(self):
        Movie.objects.create(movie_id="0437086", title="Alita: Battle Angel", year=2018, price=16.83)

    def test_index(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['movies']), 1)
        self.assertContains(response, "Movie Shop")