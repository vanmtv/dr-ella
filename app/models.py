from django.db import models

# Create your models here.

zonas = [
    ('Z1','Zona Norte'),
    ('Z2','Zona Sul'),
    ('Z3', 'Zona Leste'),
    ('Z4','Zona Oeste'),
    ('Z5','Centro')
]

class Medicos(models.Model):
    nome_Medico = models.CharField(max_length=30) 
    CRM = models.CharField(max_length=20)
    endereco = models.CharField(max_length=30)
    especialidade = models.CharField(max_length = 20)
    regiao = models.CharField(max_length=20, choices=zonas)
    

    def __str__(self):
        return self.nome_Medico