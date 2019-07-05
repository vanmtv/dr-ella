from django import forms
from app.models import Contato

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = [
            'nome',
            'email',
            'telefone',
            'mensagem'
        ]