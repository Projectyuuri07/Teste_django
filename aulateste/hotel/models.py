from django.db import models
import datetime

# Create your models here.

TIPOS_QUARTOS = (
    ("SOLTEIRO", "Solteiro"),
    ("CASAL", "Casal"),
    ("COMFORT", "Comfort"),
    ("LUXO", "Luxo")
)

class hotel(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField(max_length=500)
    logo = models.ImageField(upload_to="logo/")

    def __str__(self):
        return self.titulo

class quarto(models.Model):
    tipo = models.CharField(max_length=15, choices=TIPOS_QUARTOS)
    disponibilidade= models.IntegerField()
    valor = models.FloatField(max_length=4)
    descricao = models.TextField(max_length=200)
    foto_quarto = models.ImageField(upload_to="Foto_quartos/")
    # data_reserva = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.tipo
    
class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=100)

    def __str__(self):
        return self.nome