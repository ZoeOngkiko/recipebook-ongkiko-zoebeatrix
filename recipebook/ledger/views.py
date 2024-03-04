from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe, Ingredient, RecipeIngredient

def recipes_list(request):
    recipes = Recipe.objects.all()
    context = {'list':recipes}

    return render(request, "recipes_list.html", context)

def recipe(request, pk):
    recipe = Recipe.objects.get(pk = pk)
    context = {
        'name':recipe.name,
        'ingredients':RecipeIngredient.objects.filter(recipe__name=recipe.name)
    }

    return render(request, "recipe.html", context)