import os
from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Movie, Genre


# Create your views here.
class GenreDetailView(View):
    template_name = 'category.html'
    key = os.environ['MOVIEDB_APIKEY']

    def handle_pagination(self, movies, page_number):

        paginate_by = 18

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

    def get(self, request, *args, **kwargs):
        genre_id = kwargs.get('genre_id')
        if genre_id:
            genre = Genre.objects.filter(name=genre_id).first()
            movies = genre.movies.order_by('-year', 'movie_id')
        else:
            movies = Movie.objects.all().order_by('-year', 'movie_id')

        page_number = request.GET.get("page", 1)
        page, page_end, page_start = self.handle_pagination(movies,
                                                       page_number)

        context_dict = {
            'movies': page,
            'pages': range(page_start, page_end),
            'api_key': self.key,
        }
        return render(request, self.template_name, context=context_dict)


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
