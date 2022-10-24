from django.shortcuts import render, redirect
from .models import Filme
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
   # def homepage(request):
        #return render(request, "homepage.html")

class Homepage(TemplateView):
    template_name = "homepage.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('filme:homefilmes')
        else:
            return super() .get(request, *args, **kwargs)



#def homefilmes(request):
    #context = {}
    #lista_filmes = Filme.objects.all()
    #context['lista_filmes'] = lista_filmes
    #return render(request, "homefilmes.html", context)

class HomeFilmes(LoginRequiredMixin, ListView):
    template_name = "homefilmes.html"
    model = Filme

class Detalhesfilme(LoginRequiredMixin, DetailView):
    template_name = "detalhesfilmes.html"
    model = Filme

    def get(self, request, *args, **kwargs):
        filme = self.get_object()
        filme.visualizacoes += 1
        filme.save()
        usuario = request.user
        usuario.filmes_vistos.add(filme)
        return super() .get(request, *args, **kwargs)

class Pesquisafilme(LoginRequiredMixin, ListView):
    template_name = "pesquisa.html"
    model = Filme
    
    def get_queryset(self):
        termo_pesquisa = self.request.GET.get("query")
        if termo_pesquisa:
            object_list = self.model.objects.filter(titulo__icontains=termo_pesquisa)
            return object_list
        else:
            return None