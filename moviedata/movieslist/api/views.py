from movieslist.models import Movie
from .serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status


# function Based Views

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


@api_view(['GET','PUT','DELETE'])
def individualMovieData(request,pk):
      if request.method == 'GET':
        try:  
          movies = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'error':'Not Found'},status=status.HTTP_404_NOT_FOUND)
        serialzer = MovieSerializer(movies)
        return Response(serialzer.data)
      elif request.method == 'PUT':
          serialzer = MovieSerializer(data = request.data)
          if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data)
          else:
            return Response(serialzer.errors)
      elif request.method == 'DELETE':
           movies = Movie.objects.get(pk=pk)
           movies.delete()
           return Response(status=status.HTTP_204_NO_CONTENT)
      

# Class Based Views
# class listall(APIView):
    
#     def get(self,request):
#         movies = Movie.objects.all()
#         serialzer = MovieSerializer(movies,many=True)
#         return Response(serialzer.data)
        
          
          