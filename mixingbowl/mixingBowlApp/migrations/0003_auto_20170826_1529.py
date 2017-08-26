# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-26 19:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mixingBowlApp', '0002_ingredients_on_recipe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredients_on_recipe',
            name='ingredient',
        ),
        migrations.RemoveField(
            model_name='ingredients_on_recipe',
            name='recipe',
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(to='mixingBowlApp.Ingredient'),
        ),
        migrations.DeleteModel(
            name='Ingredients_On_Recipe',
        ),
    ]
