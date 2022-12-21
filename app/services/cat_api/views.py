import requests
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


class SearchCatApi(APIView):
    def get(self, request):

        try:
            response = requests.get(
                "https://api.thecatapi.com/v1/images/search"
            )
            cat_image_data = response.json()

            return Response(
                cat_image_data,
                status=status.HTTP_200_OK,
            )

        except Exception as error:
            error = {"error": "Não foi possível encontrar o CEP"}
            return Response(error, status=status.HTTP_404_NOT_FOUND)
