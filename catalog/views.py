import os
import sys
from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .services.user_persistence import UserPersistenceService

from .models import Movie, Genre


# Create your views here.
class GenreDetailView(View, UserPersistenceService):
    template_name = 'catalog/category.html'
    key = os.environ['MOVIEDB_APIKEY']
    default_products = 18

    def handle_pagination(self, movies, page_number):

        paginate_by = self.default_products

        paginator = Paginator(movies, paginate_by)

        try:
            page = paginator.page(page_number)
        except PageNotAnInteger:
            page_number = 1
            page = paginator.page(page_number)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)

        page_number = int(page_number)
        page_start = 1 if page_number < 5 else page_number - 3
        page_end = 6 if page_number < 5 else page_number + 2
        return page, page_end, page_start

    def genres_list(self):
        return Genre.objects.all().distinct()

    def get(self, request, *args, **kwargs):
        genre_id = kwargs.get('genre_id')
        if genre_id:
            genre = Genre.objects.filter(name=genre_id).first()
            movies = genre.movies.order_by('-year', 'movie_id')
        else:
            genre_id = 'All'
            movies = Movie.objects.all().order_by('-year', 'movie_id')

        page_number = request.GET.get("page", 1)
        page, page_end, page_start = self.handle_pagination(movies,
                                                       page_number)

        context_dict = {
            'movies': page,
            'pages': range(page_start, page_end),
            'session_id': self.session_id(request),
            'user_id': self.user_id(request),
            'api_key': self.key,
            'genre_id': genre_id,
            'genres' : self.genres_list()
        }
        return render(request, self.template_name, context=context_dict)


class MovieDetailView(View, UserPersistenceService):
    template_name = 'catalog/single-product.html'
    key = os.environ['MOVIEDB_APIKEY']

    def get(self, request, *args, **kwargs):
        movie_id = kwargs.get('movie_id')
        movie = Movie.objects.filter(movie_id=movie_id).first()
        movie_genres = movie.genres.all()

        context_dict = {
            'movie': movie,
            'session_id': self.session_id(request),
            'user_id': self.user_id(request),
            'api_key': self.key,
            'movie_genres' : movie_genres
        }
        return render(request, self.template_name, context=context_dict)


class LandingView(View, UserPersistenceService):
    template_name = 'index.html'
    key = os.environ['MOVIEDB_APIKEY']

    def get(self, request, *args, **kwargs):
        movies = Movie.objects.all().order_by('-year', 'movie_id')[:8]
        latest_movies = Movie.objects.all().order_by('-year', 'movie_id')[8:16]
        genres = Genre.objects.all()[:5]

        context_dict = {'movies': movies,
                        'latest_movies': latest_movies,
                        'session_id': self.session_id(request),
                        'user_id': self.user_id(request),
                        'genres': genres,
                        'api_key': self.key}

        return render(request, self.template_name, context=context_dict)
