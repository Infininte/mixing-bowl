from rest_framework import serializers

from .models import Ingredient, Recipe

class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = '__all__'


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(read_only=True, many=True)

    class Meta:
        model = Recipe
        fields = ('name', 'instructions', 'ingredients')