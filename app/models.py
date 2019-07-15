from django.db import models

# Create your models here.

# zonas = [
#     ('Z1','Zona Norte'),
#     ('Z2','Zona Sul'),
#     ('Z3', 'Zona Leste'),
#     ('Z4','Zona Oeste'),
#     ('Z5','Centro')
# ]

regiao = [
    ('Água Rasa', 'AR'),
    ('Anhanguera', 'AG'),
    ('Aricanduva', 'AC'),
    ('Artur Alvim','AA'),
    ('Barra Funda', 'BF'),
    ('Bela Vista', 'BV'),
    ('Belém', 'BL'),
    ('Brás', 'BR'),
    ('Butantã','BT'), 
    ('Cachoeirinha', 'CC'),
    ('Cambuci', 'CA'),
    ('Campo Belo','CB'),
    ('Campo Limpo', 'CL'),
    ('Cangaíba', 'CG'),
    ('Capão Redondo', 'CR'),
    ('Carrão', 'CO'),
    ('Casa Verde', 'CV'),
    ('Cidade Ademar', 'CM'),
    ('Cidade Dutra', 'CD'),
    ('Cidade Líder', 'CL'), 
    ('Cidade Tiradentes', 'CT'),
    ('Consolação', 'CS'),
    ('Ermelino Matarazzo', 'EM'),
    ('Freguesia do Ó', 'FO'),
    ('Guarujá', 'GU'),
    ('Guianazes', 'GN'),
    ('Iguatemi', 'IG'),
    ('Ipiranga', 'IP'),
    ('Itaim Bibi','IB'), 
    ('Itaquera', 'IT'),
    ('Jabaquara', 'JB'), 
    ('Jaguaré', 'JE'),
    ('Jardim Ângela', 'JG'),
    ('Jardim Paulista', 'JP'),
    ('Jardim São Luís', 'JS'),
    ('Lapa', 'LP'),
    ('Liberdade', 'LB'), 
    ('Limão', 'LM'),
    ('Moema', 'MO'),
    ('Mooca', 'MC'),
    ('Morumbi', 'MB'),
    ('Pedreira', 'PD'),
    ('Penha', 'PN'),
    ('Pinheiros', 'PI'),
    ('Pirituba', 'PB'),
    ('Raposo Tavares', 'RT'),
    ('República', 'RP'),
    ('Rio Pequeno', 'RQ'), 
    ('Sacomã', 'SM'),
    ('Santa Cecília', 'SC'),
    ('Santana', 'SN'),
    ('Santo Amaro', 'SA'),
    ('São Domingos', 'SD'), 
    ('Saúde', 'SU'),
    ('Sé', 'SE'),
    ('Socorro', 'SO'),
    ('Tucuruvi', 'TC'),
    ('Vila Andrade', 'VA'),
    ('Vila Curuçá', 'VC'),
    ('Vila Formosa', 'VF'),
    ('Vila Guilhermina', 'VG'),
    ('Vila Leopoldina', 'VL'),
    ('Vila Matilde', 'VM'),
    ('Vila Prudente', 'VP'),
    ('Vila Sônia', 'VS'),
]


especialidade= [
    ('Acupuntura', 'AC'),
    ('AlergiaeImunologia','AL'),
    ('Anestesiologia', 'AN'), 
    ('Angiologia', 'AG'),
    ('Cancerologia', 'CC'), 
    ('Cardiologia', 'CD'),
    ('Clínica Médica', 'CM'), 
    ('Dermatologia', 'DM'),
    ('Endocrinologia', 'EN'), 
    ('Endoscopia', 'ED'),
    ('Geriatria', 'GR'), 
    ('Ginecologia', 'GN'),
    ('Hematologia', 'HM'), 
    ('Homeopatia', 'HO'),
    ('Infectologia', 'IF'),
    ('Neurologia', 'NU'),
    ('Obstetrícia', 'OB'),
    ('Oftalmologia', 'OF'), 
    ('Ortopedia', 'OT'), 
    ('Otorrinolaringologia', 'OR'),
    ('Patologia', 'PT'), 
    ('Pediatria', 'PD'),
    ('Pneumologia', 'PM'),
    ('Psiquiatria', 'PS'),
    ('Radiologia', 'RD'),
    ('Radioterapia', 'RT'),
    ('Reumatologia', 'RM'),
    ('Urologia', 'UR'),
]

def buscar_sigla_especialidade(busca):
    for item in especialidade:
        if busca.lower() == item[0].lower():
            return item[0]
    return None

class Medico(models.Model):
    nome_Medico = models.CharField(max_length=50, default="")
    CRM = models.CharField(max_length=20, default="")
    especialidade = models.CharField(max_length = 25, choices= especialidade, default="")
    endereco = models.CharField(max_length=30, default="")
    CEP = models.CharField(max_length=9, default="")
    regiao_med = models.CharField(max_length=20, choices=regiao, default="")
    telefone = models.CharField(max_length=15, default="")
    email = models.EmailField(max_length = 40, default="")
    

    def __str__(self):
        return self.nome_Medico


class Contato(models.Model):
    nome = models.CharField(max_length=50, default="")
    email = models.EmailField(max_length=40, default="")
    telefone = models.CharField(max_length=15, default="")
    assunto = models.CharField(max_length=50, default="")
    mensagem = models.TextField(max_length=300, default="")

    def __str__(self):
        return  self.assunto

class Cadastro(models.Model):
    nome = models.CharField(max_length=50, default="")
    nascimento = models.DateField()
    telefone = models.CharField(max_length=15, default="")
    email = models.EmailField(max_length=50, default="")
    username = models.CharField(max_length=20, default="")
    password = models.CharField(max_length=20, default="")

    def __str__(self):
        return  self.username