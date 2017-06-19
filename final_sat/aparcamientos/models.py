from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Parking(models.Model):
    id_entidad = models.IntegerField()
    nombre = models.CharField(max_length=256)
    descripcion = models.TextField()
    accesibilidad = models.IntegerField()
    url = models.CharField(max_length=256)
    direccion = models.CharField(max_length=256)
    barrio = models.CharField(max_length=256)
    distrito = models.CharField(max_length=256)
    latitud = models.CharField(max_length=256)
    longitud = models.CharField(max_length=512)
    contacto = models.TextField(max_length=256, default="NO HAY DATOS")


class Selected_Parking(models.Model):
    id_entidad = models.ForeignKey(Parking)
    usuario = models.ForeignKey(User, default="")
    fecha = models.DateField(auto_now_add=True)


class Comments(models.Model):
    id_entidad = models.ForeignKey(Parking)
    comentario = models.TextField()

class Style_CSS(models.Model):
    usuario = models.ForeignKey(User, default="")
    titulo = models.CharField(max_length=256)
