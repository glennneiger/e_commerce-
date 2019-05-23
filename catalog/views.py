import os
from django.shortcuts import render
from django.views import View

from .models import Movie, Genre


# Create your views here.
class MovieDetailView(View):
    template_name = 'single-product.html'
    key = os.environ['MOVIEDB_APIKEY']

    def get(self, request, *args, **kwargs):
        movie_id = kwargs.get('movie_id')
        movie = Movie.objects.filter(movie_id=movie_id).first()
        movie_genres = movie.genres.all()

        context_dict = {
            'movie': movie,
            'api_key': self.key,
            'movie_genres' : movie_genres
        }
        return render(request, self.template_name, context=context_dict)


class LandingView(View):
    template_name = 'index.html'
    key = os.environ['MOVIEDB_APIKEY']

    def get(self, request, *args, **kwargs):
        movies = Movie.objects.all().order_by('-year', 'movie_id')[:8]
        latest_movies = Movie.objects.all().order_by('-year', 'movie_id')[8:16]
        genres = Genre.objects.all()[:5]

        context_dict = {'movies': movies,
                        'latest_movies': latest_movies,
                        'genres': genres,
                        'api_key': self.key}

        return render(request, self.template_name, context=context_dict)
