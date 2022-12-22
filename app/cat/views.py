import requests

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import CatBreeds
from .serializers import CatBreedsSerializer
        

class CatBreedsViewSet(ModelViewSet):
    
    def list(self, _):
        url = f"https://api.thecatapi.com/v1/breeds"
        response = requests.get(url)
        data = response.json()
        serializer_class = CatBreedsSerializer

        try:
            if data:
                for value in data:
                    _ = CatBreeds.objects.get_or_create(
                        id_breeds=value["id"],
                        name=value["name"],
                        origin=value["origin"],
                        temperament=value["temperament"],
                        description=value["description"]
                    )
            else:
                error = {"error": "Not found result data"}
                return Response(error, status=status.HTTP_400_NOT_FOUND)
            
            queryset = CatBreeds.objects.all()
            serializer = serializer_class(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as error:
            print(error)
            error = {"error": "Error internal server API Cats"}
            return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
