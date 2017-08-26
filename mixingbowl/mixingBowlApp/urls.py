from django.conf.urls import url

from .api import RecipeApi, IngredientApi

urlpatterns = [
    url(r'^ingredients$', IngredientApi.as_view()),
    url(r'^recipes$', RecipeApi.as_view())
]