from rest_framework.serializers import ModelSerializer

from .models import CatBreeds


class CatBreedsSerializer(ModelSerializer):
    class Meta:
        model = CatBreeds
        fields = "__all__"
