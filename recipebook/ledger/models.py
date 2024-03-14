from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ingredient', args=[str(self.pk)])   #returns the URL with the specified name, and can pass arguments to the function

class Recipe(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ledger:recipe', args=[str(self.pk)])

class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=50)
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='recipe'
    )

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingredients'
    )

    def __str__(self):
        return f'{self.ingredient} for {self.recipe}'
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bio = models.TextField()

    def __str__(self):
        return self.name


