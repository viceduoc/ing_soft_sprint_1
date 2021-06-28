from django.db import models

# Create your models here.

class Residente(models.Model):
    id = models.IntegerField(primary_key=True)
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    fechaNacimiento = models.DateField()
    
    def __str__(self):
        return self.nombre + self.apellido


class Pieza(models.Model):
    id = models.IntegerField(primary_key=True)
    nroPieza = models.IntegerField()
    estado = models.BooleanField(default=True)
    residente = models.ForeignKey(Residente, blank=True, null=True, on_delete=models.CASCADE)