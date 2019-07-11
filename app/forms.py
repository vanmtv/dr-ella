from django import forms
from app.models import Contato, Cadastro

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = [
            'nome',
            'email',
            'telefone',
            'assunto',
            'mensagem'
        ]

class CadastroForm(forms.ModelForm):
    class Meta:
        model = Cadastro
        fields = [
            'nome',
            'email',
            'nascimento',
            'telefone',
            'username',
            'password'
        ]

class LoginForm(forms.Form):
    username = forms.CharField(label='username')
    password = forms.CharField(label= 'password', widget=forms.PasswordInput())

class BuscaForm(forms.Form):
    search = forms.CharField(label='pesquisa')
