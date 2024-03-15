from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from .models import Ingredient, Recipe, RecipeIngredient


def recipes_list(request):
    recipes = Recipe.objects.all()
    context = {"list": recipes}

    return render(request, "recipes_list.html", context)


@login_required
def recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    context = {
        "name": recipe.name,
        "author": recipe.author,
        "created_on": recipe.created_on,
        "updated_on": recipe.updated_on,
        "ingredients": RecipeIngredient.objects.filter(recipe__name=recipe.name),
    }

    return render(request, "recipe_detail.html", context)
