from django.shortcuts import render
from rest_framework_json_api.views import ModelViewSet
from cart.serializers import ProductSerializer
from catalog.models import Movie

def index(request):
    return render(request, 'cart/index.html')

# Create your views here.
class ProductViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = ProductSerializer