from django.shortcuts import render
from . models import Movie
from django.http import JsonResponse

def getMovies(request):
    movies = Movie.objects.all()
    response = {
        'movies':list(movies.values())
    }
    return JsonResponse(response)

def getIndividualMovies(request,pk):
    movies = Movie.objects.get(pk=pk)
    response = {
       'name':movies.name,
       'description':movies.description,
       'active':movies.active,
    }
    return JsonResponse(response)
