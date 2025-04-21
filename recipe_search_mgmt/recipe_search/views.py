from django.shortcuts import render
from django.http import HttpResponse
from . import models, urls

def recipe_search_home(request):
    return HttpResponse("This is the recipe_search app homepage via recipe_search/views.py")


def recipe_search_about(request):
    return HttpResponse("This is the recipe_search about page via ..mgmt/views.py")


def recipe_search_recipes(request):
    recipes =[]
    image_url = settings.STATIC_URL + 'recipe_search/images/image.png'
    context = { 'recipes': recipes,
                'image':  image_url
               }
    return render(request, 'main.html', context)
