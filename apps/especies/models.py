from django.db import models
from common.utils import TIPOS

class UpperCaseCharField(models.CharField):
    def __init__(self, *args, **kwargs):
        super(UpperCaseCharField, self).__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        value = getattr(model_instance, self.attname, None)
        if value:
            value = value.upper()
            setattr(model_instance, self.attname, value)
            return value
        else:
            return super(UpperCaseCharField, self).pre_save(model_instance, add)


class EspeciesManager(models.Manager):
    def se_depura(self):
        self.filter(depuracion=True)

class Especies(models.Model):
    '''Lista de especies'''
    fao = UpperCaseCharField(
        max_length=3,
        verbose_name='Código FAO',
        blank=False,
        null=False,)
    n_cientifico = models.CharField(
        max_length=30,
        verbose_name='Nombre científico',
        blank=False,
        null=False,)
    n_comercial = models.CharField(
        max_length=30,
        verbose_name='Nombre comercial',
        blank=False,
        null=False,)
    tipo = models.CharField(
        max_length=20,
        choices=TIPOS,
        default='bivalvos',
        verbose_name='Tipo',)
    depuracion = models.BooleanField(
        verbose_name='¿Depuración en Mercamaris?',
        default=False,)

    class Meta:
        verbose_name = 'Especie'
        verbose_name_plural = 'Especies'
        ordering = ['n_comercial']

    def __str__(self):
        return str(self.n_comercial)
