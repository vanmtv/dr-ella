from django.db import models

# Create your models here.

zonas = [
    ('Z1','Zona Norte'),
    ('Z2','Zona Sul'),
    ('Z3', 'Zona Leste'),
    ('Z4','Zona Oeste'),
    ('Z5','Centro')
]

class Medico(models.Model):
    nome_Medico = models.CharField(max_length=30, default="")
    CRM = models.CharField(max_length=20, default="")
    especialidade = models.CharField(max_length = 20, default="")
    endereco = models.CharField(max_length=30, default="")
    CEP = models.CharField(max_length=9, default="")
    regiao = models.CharField(max_length=20, choices=zonas, default="")
    telefone = models.CharField(max_length=15, default="")
    email = models.CharField(max_length = 40, default="")
    

    def __str__(self):
        return self.nome_Medico


class Contato(models.Model):
    nome = models.CharField(max_length=30, default="")
    email = models.CharField(max_length=40, default="")
    telefone = models.CharField(max_length=15, default="")
    mensagem = models.CharField(max_length=300, default="")

    def __str__(self):
        return  self.nome