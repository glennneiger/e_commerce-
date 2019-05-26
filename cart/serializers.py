from rest_framework_json_api import  serializers
from catalog.models import Movie


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

