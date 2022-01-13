from django.db import models


class Empresa(models.Model):
    '''Tabla de empresas'''
    denominacion = models.CharField(
        verbose_name='Denominación social/Apellidos y nombre',
        max_length=60)
    n_comercial = models.CharField(
        verbose_name='Nombre comercial',
        max_length=50,
        blank=True,
        null=True,)
    calle = models.CharField(
        verbose_name='Calle',
        max_length=100)
    calle2 = models.CharField(
        verbose_name='Calle 2',
        max_length=100,
        blank=True, null=True)
    ciudad = models.CharField(
        verbose_name='Ciudad',
        max_length=30,
        blank=True, null=True)
    provincia = models.CharField(
        verbose_name='Provincia',
        max_length=20,
        blank=True, null=True)
    cp = models.CharField(
        verbose_name='Código Postal',
        max_length=8,
        blank=True, null=True)
    pais = models.CharField(
        verbose_name='País',
        max_length=20,
        default='España')
    nif = models.CharField(
        verbose_name='NIF',
        max_length=15,
        unique=True,
        error_messages={'unique': 'Ya existe otro contacto con ese NIF'})
    rgsea = models.CharField(
        verbose_name='RGSEAA',
        max_length=15,
        blank=True, null=True)
    email = models.EmailField(
        verbose_name='Email',
        blank=True, null=True)
    tfno = models.CharField(
        verbose_name='Teléfono ejemplo +34000000000',
        max_length=12,
        blank=True, null=True)
    movil = models.CharField(
        verbose_name='Móvil ejemplo +34000000000',
        max_length=12,
        blank=True, null=True)
    cliente = models.BooleanField(
        verbose_name='Cliente',
        blank=True, null=True)
    proveedor = models.BooleanField(
        verbose_name='Proveedor',
        blank=True, null=True)
    codigo = models.CharField(
        max_length=3,
        verbose_name='Código de proveedor',
        unique=True,
        blank=True, null=True,)
    proveedor_aprobado = models.BooleanField(
        verbose_name='¿Proveedor aprobado?',
        default=False,)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        if self.n_comercial:
            return f'{self.n_comercial}'
        else:
            return f'{self.denominacion}'


class ProveedorManager(models.Manager):
    def proveedor_marisco(self):
        return self.filter(codigo__isnull=False, proveedor=True, proveedor_aprobado =True)
    def proveedor(self):
        return self.filter(proveedor=True)

class Proveedor(Empresa):

    objects = ProveedorManager()

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        proxy = True

    def __str__(self):
        return str(self.n_comercial)


class Contacto(models.Model):
    nombre = models.CharField(
        max_length=50,
        verbose_name='Nombre de contacto',
        blank=False, null=False, )
    empresa = models.ForeignKey(
        Empresa,
        on_delete=models.CASCADE,
        related_name='empresas',)
    email = models.EmailField(
        verbose_name='Email',
        blank=True, null=True)
    tfno = models.CharField(
        verbose_name='Teléfono ejemplo +34000000000',
        max_length=12,
        blank=True, null=True)

    def __str__(self):
        return str(self.nombre) + " " + str(self.empresa)
