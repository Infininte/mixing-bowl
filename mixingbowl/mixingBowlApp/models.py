from django.db import models
from django.utils.encoding  import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class Ingredient(models.Model):
    name = models.CharField(max_length=150)
    category = models.CharField(max_length=100)

    def __str__(self):
        return "Ingredient: {}".format(self.name)

@python_2_unicode_compatible
class Recipe(models.Model):
    name = models.CharField(max_length = 50)
    instructions = models.TextField(blank = True)
    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self):
        return "Recipe: {}".format(self.name)