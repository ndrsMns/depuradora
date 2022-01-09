from django.db import models

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

class Especies(models.Model):
    '''Lista de especies'''
    fao = UpperCaseCharField(
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
        verbose_name = 'Nombre comercial',
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
