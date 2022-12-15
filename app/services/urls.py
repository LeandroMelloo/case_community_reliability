from django.urls import path
from .views import SearchCatApi

urlpatterns = [
    path("images/search/", SearchCatApi.as_view(), name="cat_api"),
]