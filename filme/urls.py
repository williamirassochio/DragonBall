from django.urls import path, include
from .views import HomeFilmes, Homepage, Detalhesfilme, Pesquisafilme
from django.contrib.auth import views as auth_view
app_name = 'filme'

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('filmes/', HomeFilmes.as_view(), name='homefilmes'),
    path('filmes/<int:pk>', Detalhesfilme.as_view(), name='detalhesfilmes'),
    path('pesquisa/', Pesquisafilme.as_view(), name= 'pesquisafilme'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name= 'login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name= 'logout'),
]
