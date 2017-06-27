from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone


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
    color = models.CharField(max_length=256, default="#040E4C")
    background = models.CharField(max_length=256, default="#8FE7D5")
    font_size = models.IntegerField(default=15)


class Users_Favs(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    id_entidad = models.IntegerField()
    fecha = models.DateTimeField(default = timezone.now())


class Comment(models.Model):
    id_entidad = models.IntegerField()
    titulo = models.TextField(max_length=256, default="Sin título")
    texto = models.TextField(max_length=256)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(default = timezone.now())
