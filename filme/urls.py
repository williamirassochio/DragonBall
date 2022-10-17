from django.urls import path, include
from .views import HomeFilmes, Homepage, Detalhesfilme, Pesquisafilme

app_name = 'filme'

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('filmes/', HomeFilmes.as_view(), name='homefilmes'),
    path('filmes/<int:pk>', Detalhesfilme.as_view(), name='detalhesfilmes'),
    path('pesquisa/', Pesquisafilme.as_view(), name= 'pesquisafilme')
]
