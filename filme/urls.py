from django.urls import path, include
from .views import HomeFilmes, Homepage, Detalhesfilme

urlpatterns = [
    path('', Homepage.as_view()),
    path('filmes/', HomeFilmes.as_view()),
    path('filmes/<int:pk>', Detalhesfilme.as_view()),
]
