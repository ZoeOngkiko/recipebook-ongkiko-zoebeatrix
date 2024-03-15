from django.urls import path

from .views import recipe, recipes_list

urlpatterns = [
    path("recipes/list", recipes_list, name="list"),
    path("recipe/<int:pk>/", recipe, name="recipe"),
]

app_name = "ledger"
