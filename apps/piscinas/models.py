from django.db import models


class Zonas(models.Model):
    nombre_zona = models.CharField(
        max_length=30,
        verbose_name='Nombre Zona')
    ubicacion = models.CharField(
        max_length=100,
        verbose_name='Ubicación')

    class Meta:
        verbose_name = 'Zona'
        verbose_name_plural = 'Zonas'
        ordering = ['nombre_zona']

    def __str__(self):
        return self.nombre_zona


class Piscinas(models.Model):
    no_piscina = models.CharField(
        max_length=30,
        verbose_name='Número piscina')
    zona = models.ForeignKey(
        Zonas,
        on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Piscina'
        verbose_name_plural = 'Piscinas'
        ordering = ['no_piscina']

    def __str__(self):
        return self.no_piscina
