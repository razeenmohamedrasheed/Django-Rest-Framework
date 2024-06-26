from movieslist.models import Movie
from .serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET','POST'])
def movieList(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serialzer = MovieSerializer(movies,many=True)
        return Response(serialzer.data)
    elif request.method == 'POST':
        serialzer = MovieSerializer(data = request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data)
        else:
            return Response(serialzer.errors)


@api_view(['GET','PUT'])
def individualMovieData(request,pk):
      if request.method == 'GET':
        movies = Movie.objects.get(pk=pk)
        serialzer = MovieSerializer(movies)
        return Response(serialzer.data)
      elif request.method == 'PUT':
          serialzer = MovieSerializer(data = request.data)
          if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data)
          else:
            return Response(serialzer.errors)
          