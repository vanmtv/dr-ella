from django.contrib import admin
from app.models import Medico, Contato, Cadastro

# Register your models here.

admin.site.register(Medico)
admin.site.register(Contato)
admin.site.register(Cadastro)