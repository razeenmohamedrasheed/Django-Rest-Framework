from django.urls import path 
from . import views

urlpatterns = [
    path('',views.movieList,name="list"),
    path('<int:pk>',views.individualMovieData,name="individual"),
]
