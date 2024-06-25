from django.shortcuts import render
from . models import Movie
from django.http import JsonResponse

def getMovies(request):
    movies = Movie.objects.all()
    response = {
        'movies':list(movies.values())
    }
    return JsonResponse(response)
