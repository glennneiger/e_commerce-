from django.urls import include, path
from rest_framework import routers

from cart.views import ProductViewSet, index

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'api/products', ProductViewSet)

urlpatterns = [
    path('cart/', index),
    path('', include(router.urls)),
]
