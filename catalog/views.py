from django.shortcuts import render
from django.views import View

from .models import Movie

# Create your views here.
class LandingView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        movie = Movie.objects.first()
        print(movie.description, movie.price)
        return render(request, self.template_name)
