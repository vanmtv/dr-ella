from django import forms
from app.models import Contato
from app.models import Cadastro
# from app.models import Login

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
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Cadastro
        fields = [
            'nome',
            'email',
            'nascimento',
            'telefone',
            'username'
        ]

# class LoginForm(forms.ModelForm):
#     username = forms.CharField(max_lentgh=20)
#     password = forms.CharField(max_lentgh=20, widget=forms.PasswordInput)