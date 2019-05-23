from django.urls import path
from .views import LandingView, MovieDetailView

urlpatterns = [
    path('movies/<str:movie_id>', MovieDetailView.as_view(), name='movie_detail'),
    path('', LandingView.as_view()),
]
