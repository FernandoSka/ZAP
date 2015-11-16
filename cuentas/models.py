from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Datosextra(models.Model):
    """docstring for telefono"""
    id_persona = models.ForeignKey(User)
    tel = models.IntegerField(null=True, blank=True)
    fecha = models. DateField(auto_now=False, auto_now_add=False)


class Tipnot(models.Model):
    """docstring for tip_not"""
    tipo = models.CharField(max_length=None, blank=False)


class Noticia(models.Model):
    """docstring for noticia"""
    id_persona = models.ForeignKey(User)
    id_tipo = models.ForeignKey(Tipnot)


class Amigo(models.Model):
    """docstring for Amigo"""
    id_persona = models.ForeignKey(User)
    id_persona2 = models.ForeignKey(User)
