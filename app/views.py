from django.shortcuts import render
from app.forms import ContatoForm

# Create your views here.

def mostrar_home(request):
    return render (request, 'home.html')

def mostrar_sobre_nos(request):
    return render(request, 'sobre-nos.html')

def mostrar_busca(request):
    return render(request, 'busca.html')

def mostrar_contato(request):
    return render(request, 'contato.html')

