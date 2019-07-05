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
    nome_Medico = models.CharField(max_length=30)
    CRM = models.CharField(max_length=20)
    especialidade = models.CharField(max_length = 20)
    endereco = models.CharField(max_length=30)
    CEP = models.CharField(max_length=9)
    regiao = models.CharField(max_length=20, choices=zonas)
    telefone = models.CharField(max_length=15)
    email = models.CharField(max_length = 40)
    

    def __str__(self):
        return self.nome_Medico


class Contato(models.Model):
    nome = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    telefone = models.CharField(max_length=15)
    mensagem = models.CharField(max_length=300)

    def __str__(self):
        return  self.nome