from movieslist.models import Movie
from .serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def movieList(request):
    movies = Movie.objects.all()
    serialzer = MovieSerializer(movies,many=True)
    return Response(serialzer.data)

@api_view(['GET'])
def individualMovieData(request,pk):
    movies = Movie.objects.get(pk=pk)
    serialzer = MovieSerializer(movies)
    return Response(serialzer.data)