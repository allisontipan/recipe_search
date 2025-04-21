from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.recipe_search_home, name='recipe_search_home'),
    path('about/', views.recipe_search_about, name='recipe_search_about'),
    path('recipes/', views.recipe_search_recipes, name='recipe_search_recipes')
]
