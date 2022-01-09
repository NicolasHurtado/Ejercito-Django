from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
tipoarma_choice = [
    ('cuchillos', 'cuchillos'),
    ('lanzas', 'lanzas'),
    ('martillos', 'martillos'),
    ('espadas', 'espadas')
]

class Arma(models.Model):
    tipo = models.CharField(max_length=255, choices=tipoarma_choice)
    nombre = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nombre.capitalize()

estados_choice = [
    ('nuevo', 'nuevo'),
    ('frente', 'frente'),
    ('caido', 'caido'),
    ('herido', 'herido')
]

class Soldado(models.Model):
    apodo = models.CharField(max_length=255, unique=True)
    estado = models.CharField(max_length=50, choices=estados_choice, default='nuevo')
    arma = models.ForeignKey(Arma, on_delete=models.CASCADE)
    def __str__(self):
        return self.apodo