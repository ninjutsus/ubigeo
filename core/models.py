
from django.db import models
from django.core.urlresolvers import reverse


class Pais(models.Model):
    nombre = models.TextField(max_length=150)
    codigo = models.CharField(max_length=5)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = u'Paises'

class Departamento(models.Model):
    nombre = models.TextField(max_length=150)
    pais = models.ForeignKey(Pais, related_name="departamentos")

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = u'Departamentos'


class Provincia(models.Model):
    nombre = models.TextField(max_length=150)
    departamento = models.ForeignKey(Departamento, related_name="provincias")

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = u'Provincias'

class Distrito(models.Model):
    nombre = models.TextField(max_length=150)
    provincia = models.ForeignKey(Provincia, related_name="distritos")

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = u'Distritos'



