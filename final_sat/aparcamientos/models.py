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
    likes = models.IntegerField(default=0)
    n_comentarios = models.IntegerField(default=0)


class Users_Page(models.Model):
    usuario = models.OneToOneField(User, related_name="usuario")
    titulo = models.TextField(max_length=256, null=True)
    color = models.CharField(max_length=256, null=True)
    background = models.CharField(max_length=256, null=True)
    font_size = models.IntegerField(null=True)
