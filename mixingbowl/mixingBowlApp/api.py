from rest_framework.generics import ListAPIView

from .serializers import RecipeSerializer, IngredientSerializer
from .models import Recipe, Ingredient

class IngredientApi(ListAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class RecipeApi(ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer