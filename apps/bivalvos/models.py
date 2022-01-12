from django.db import models
from django.core.validators import RegexValidator

from apps.contactos.models import Empresa
from apps.especies.models import Especies
from apps.piscinas.models import Piscinas

from common.utils import LISTA_ARTES, LISTA_M_PRODUCCION


class DocRegistro(models.Model):
    no_doc_registro = models.CharField(
        max_length=14,
        primary_key=True,
        verbose_name='Número documento Registro',
        validators=[RegexValidator(
            regex=r"\d{4}.\d{9}",
            message='Formato de código no válido',
            code='nomatch')]
    )
    n_recolector = models.ForeignKey(
        Empresa,
        on_delete=models.PROTECT,
        limit_choices_to={'proveedor': True})
    fecha_recoleccion = models.DateField(
        auto_now_add=False,
        verbose_name='Fecha recolección')
    cliente = models.ForeignKey(
        Empresa,
        on_delete=models.PROTECT,
        limit_choices_to={'cliente': True})
    destino = models.CharField(
        max_length=100,
        default='MercaMaris Nº RGSEAA: 12.021608/C',
        verbose_name='Destino')
    zona_gal = models.CharField(
        max_length=50,
        null=True, blank=True,
        verbose_name='Nombre zona GAL')
    zona_biotoxina = models.CharField(
        max_length=100,
        verbose_name='Nombre zona biotoxina')
    c_sanitaria = models.CharField(
        max_length=1,
        verbose_name='Calificación sanitaria')
    verificacion_toxinas = models.BooleanField(
        editable=True,
        blank=True, null=True,
        verbose_name='Zona biotoxinas abierta?')

    class Meta:
        verbose_name = 'Documento de registro'
        verbose_name_plural = 'Documentos de registro'
        ordering = ['no_doc_registro']

    def __str__(self):
        return self.no_doc_registro


class EntradaBivalvos(models.Model):
    especie = models.ForeignKey(
        Especies,
        on_delete=models.PROTECT,
        related_name='entradas',
        related_query_name='entrada'
    )
    lote = models.CharField(
        verbose_name='Lote',
        max_length=40,
        editable=False,
    )
    cantidad_recibida = models.DecimalField(
        verbose_name='Cantidad recibida',
        max_digits=10,
        decimal_places=2
    )
    fecha_hora_entrada = models.DateTimeField(
        verbose_name='Fecha y hora entrada'
    )
    piscina = models.ForeignKey(
        Piscinas,
        on_delete=models.PROTECT
    )
    ria_pais = models.CharField(
        verbose_name='Ría/País',
        max_length=30
    )
    m_produccion = models.CharField(
        max_length=25,
        verbose_name='Método de producción',
        choices=LISTA_M_PRODUCCION,
        blank=True, null=True,
    )
    arte = models.CharField(
        max_length=30,
        verbose_name='Arte de Pesca',
        choices=LISTA_ARTES,
        blank=True, null=True,
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.lote


class EntradaBivalvosDepuracion(EntradaBivalvos):
    doc_registro = models.ForeignKey(
        DocRegistro,
        on_delete=models.PROTECT,
        related_name='entradas',
        related_query_name='entrada',
    )

    def save(self, *args, **kwargs):
        if not self.lote:
            fin_lote = '00'
            if EntradaBivalvosDepuracion.objects.all().order_by('id').last() is not None:
                ultimo_lote = EntradaBivalvosDepuracion.objects.all().order_by('id').last()
                if ultimo_lote.lote[0:6] == str(self.doc_registro.no_doc_registro[-6:]):
                    id_ultimo_lote = int(ultimo_lote.lote[-2:])
                    fin_lote = str(id_ultimo_lote + 1).zfill(2)
            nuevo_lote = (
                str(self.doc_registro)[-6:] +
                self.fecha_entrada.strftime("%Y%m%d") +
                Especies.objects.get(n_comercial=self.especie).c_FAO +
                fin_lote)
            self.lote = nuevo_lote
            super(EntradaBivalvosDepuracion, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Entrada bivalvos depuración'
        verbose_name_plural = 'Entradas bivalvos depuración'
        ordering = ['id']

    def __str__(self):


class EntradaBivalvosDepuracion(EntradaBivalvos):
    doc_registro = models.ForeignKey(
        DocRegistro,
        on_delete=models.PROTECT,
        related_name='entradas',
        related_query_name='entrada',
    )

    def save(self, *args, **kwargs):
        if not self.lote:
            fin_lote = '00'
            if EntradaBivalvosDepuracion.objects.all().order_by('id').last() is not None:
                ultimo_lote = EntradaBivalvosDepuracion.objects.all().order_by('id').last()
                if ultimo_lote.lote[0:6] == str(self.doc_registro.no_doc_registro[-6:]):
                    id_ultimo_lote = int(ultimo_lote.lote[-2:])
                    fin_lote = str(id_ultimo_lote + 1).zfill(2)
            nuevo_lote = (
                str(self.doc_registro)[-6:] +
                self.fecha_entrada.strftime("%Y%m%d") +
                Especies.objects.get(n_comercial=self.especie).c_FAO +
                fin_lote)
            self.lote = nuevo_lote
            super(EntradaBivalvosDepuracion, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Entrada bivalvos depuración'
        verbose_name_plural = 'Entradas bivalvos depuración'
        ordering = ['id']

    def __str__(self):
        return self.lote
