from django.urls import path
from .views import CatBreedsViewSet

urlpatterns = [
    path(
        "cat_breeds", CatBreedsViewSet.as_view({"get": "list"}),
        name="cat_breeds"
    ),
]
