from django.db import models

# Create your models here.
class Especies(models.Model):
    '''Lista de especies'''
    fao = models.CharField(
        max_length = 3,
        verbose_name = 'Código FAO',
        blank=False,
        null=False,
    )
    n_cientifico = models.CharField(
        max_length = 30,
        verbose_name = 'Nombre científico',
        blank=False,
        null=False,
    )
    n_comercial = models.CharField(
        max_length = 30,
        verbose_name = 'Nombre Comercial',
        blank=False,
        null=False,
    )
    depuracion = models.BooleanField(
        verbose_name='¿Depuración en Mercamaris?',
        default=False,
    )
    class Meta:
        verbose_name = 'Especie'
        verbose_name_plural = 'Especies'

    def __str__(self):
        return str(self.n_comercial)
