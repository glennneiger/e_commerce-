from django.urls import path
from .views import LandingView, MovieDetailView, GenreDetailView

urlpatterns = [
    path('movies/<str:movie_id>', MovieDetailView.as_view(), name='movie_detail'),
    path('genres/', GenreDetailView.as_view(), {'genre_id': None} ,name='genres'),
    path('genres/<str:genre_id>', GenreDetailView.as_view(), name='genre_detail'),
    path('', LandingView.as_view()),
]
