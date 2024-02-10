from django.db import models

# Create your models here.

class Jugador(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni = models.IntegerField()
    numero_sorteado = models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.dni} = {self.numero_sorteado}"