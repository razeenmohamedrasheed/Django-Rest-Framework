from django.urls import path 
from . import views

urlpatterns = [
    path('',views.getMovies,name="list"),
    path('<int:pk>',views.getIndividualMovies,name="individual"),
]
