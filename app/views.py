from django.shortcuts import render
from app.forms import ContatoForm
from app.forms import CadastroForm
# from app.forms import LoginForm

# Create your views here.

def mostrar_home(request):
    return render (request, 'home.html')

def mostrar_sobre_nos(request):
    return render(request, 'sobre-nos.html')

def mostrar_busca(request):
    return render(request, 'busca.html')

def mostrar_contato(request):
    formulario = ContatoForm(request.POST or None)
    msg = ''

    if formulario.is_valid():
        formulario.save()
        formulario = ContatoForm()
        msg = 'Mensagem enviada com sucesso'

    contexto = {
        'form' : formulario,
        'msg' : msg
    }
    return render(request, 'contato.html', contexto)
#    return render(request, 'contato.html')

def mostrar_cadastro(request):
    formulario_cadastro = CadastroForm(request.POST or None)
    msg = ''

    if formulario_cadastro.is_valid():
        formulario_cadastro.save()
        formulario_cadastro = CadastroForm()
        msg = 'Cadastro criado com sucesso'

    contexto = {
        'form' : formulario_cadastro,
        'msg' : msg
    }

    return render(request, 'cadastro.html', contexto)

def mostrar_funciona(request):
    return render(request, 'funciona.html')

def mostrar_login(request):
    return  render(request, 'login.html')
