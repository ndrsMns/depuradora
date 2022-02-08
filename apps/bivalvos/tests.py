from datetime import datetime
from django.utils import timezone
from django.test import TestCase

from .models import DocRegistro, EntradaBivalvosDepuracion
from apps.contactos.models import Empresa, Proveedor
from apps.especies.models import Especies
from apps.piscinas.models import Piscinas, Zonas

NOW = timezone.now()
LOTE_DATE =NOW.date().strftime('%y%m%d')

class BaseModelTestCase(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.cli = Empresa.objects.create(
            denominacion='Depuradora',
            calle='Corcubion',
            proveedor=True,
            nif='B70583539',
            rgsea='rgsea',
            codigo='LCC',
            cliente=True,
            proveedor_aprobado=True)

        cls.recolector = Empresa.objects.create(
            denominacion='Recolector1',
            calle='Carril',
            cliente=False,
            proveedor=True,
            nif='B00000000',
            rgsea='rgsea',
            codigo='LCR',
            proveedor_aprobado=True)

        cls.doc_registro = DocRegistro.objects.create(
            no_doc_registro='2022R000000000',
            n_recolector=cls.recolector,
            fecha_recoleccion=NOW,
            cliente=cls.cli,
            zona_gal='GAL-09/06',
            zona_biotoxina='ARO-V',
            c_sanitaria='B',
            verificacion_toxinas=True)

        cls.zona = Zonas.objects.create(
            nombre_zona='depuradora', 
            ubicacion='Corcubion')

        cls.piscina = Piscinas.objects.create(
            zona = cls.zona, 
            no_piscina ='Piscina1')

        cls.especie = Especies.objects.create(
            fao='coc', 
            n_cientifico= 'Cerastoderma edule', 
            n_comercial='Berberecho', 
            depuracion=True)
        cls.especie2 = Especies.objects.create(
            fao='clj', 
            n_cientifico= 'Ruditapes philippinarum', 
            n_comercial='Almeja japonesa', 
            depuracion=True)
        #str_dt =now
        #dt= timezone.strptime(str_dt, '%Y-%m-%d %H:%M:%S')

        cls.entrada1 = EntradaBivalvosDepuracion.objects.create(
            doc_registro= DocRegistro.objects.get(no_doc_registro='2022R000000000'),
            especie=cls.especie,
            cantidad_recibida= 10,
            fecha_hora_entrada=NOW,
            piscina= cls.piscina,
            ria_pais='Ria de Arousa',
            m_produccion= 'capturado',
            arte='Raños',
        )
        cls.entrada2 = EntradaBivalvosDepuracion.objects.create(
            doc_registro= DocRegistro.objects.get(no_doc_registro='2022R000000000'),
            especie=cls.especie2,
            cantidad_recibida= 20,
            fecha_hora_entrada=NOW,
            piscina= cls.piscina,
            ria_pais='Ria de Arousa',
            m_produccion= 'capturado',
            arte='Raños',
        )
        cls.entrada3 = EntradaBivalvosDepuracion.objects.create(
            doc_registro= DocRegistro.objects.get(no_doc_registro='2022R000000000'),
            especie=cls.especie,
            cantidad_recibida= 20,
            fecha_hora_entrada=NOW,
            piscina= cls.piscina,
            ria_pais='Ria de Arousa',
            m_produccion= 'capturado',
            arte='Raños',
        )

class DocumentoRegTest(BaseModelTestCase):
    def test_doc_registro_create(self):
        print (NOW.date)
        self.assertEqual(str(self.doc_registro.n_recolector), 'Recolector1')
        self.assertEqual(self.doc_registro.n_recolector.denominacion, 'Recolector1')
        self.assertEqual(self.doc_registro.fecha_recoleccion, NOW)
        self.assertEqual(str(self.doc_registro.cliente.denominacion), 'Depuradora')
        self.assertEqual(self.doc_registro.cliente.denominacion, 'Depuradora')
        self.assertEqual(self.doc_registro.destino, 'MercaMaris Nº RGSEAA: 12.021608/C')
        self.assertEqual(self.doc_registro.zona_gal,'GAL-09/06')
        self.assertEqual(self.doc_registro.zona_biotoxina,'ARO-V')
        self.assertEqual(self.doc_registro.c_sanitaria,'B')
        self.assertEqual(self.doc_registro.verificacion_toxinas, True)



class EntradaBivalvosDepuTest(BaseModelTestCase):

    def test_entrada_biv_depu_create(self):
        print (self.entrada1.fecha_entrada)
        self.assertEqual(self.entrada1.especie.n_comercial,'Berberecho')
        self.assertEqual(self.entrada1.cantidad_recibida, 10,)
        self.assertEqual(self.entrada1.fecha_hora_entrada, NOW)
        self.assertEqual(self.entrada1.piscina.no_piscina, 'Piscina1')
        self.assertEqual(self.entrada1.ria_pais,'Ria de Arousa')
        self.assertEqual(self.entrada1.m_produccion, 'capturado')
        self.assertEqual(self.entrada1.arte,'Raños')
        self.assertEqual(self.entrada1.lote, LOTE_DATE+'COCLCR001')
    
    def test_entrada_manager(self):
        print ('Filtro por Fecha: ',
            EntradaBivalvosDepuracion.objects.filter_by_date(
                self.entrada1.fecha_entrada).count())
        self.assertEqual(EntradaBivalvosDepuracion.objects.filter_by_date(
            self.entrada1.fecha_entrada).count(), 3)
        print ('Filtro por Fecha y especie: ',
            EntradaBivalvosDepuracion.objects.filter_by_date_especie(
                self.entrada1.fecha_entrada, self.entrada1.especie).count())
        self.assertEqual(EntradaBivalvosDepuracion.objects.filter_by_date_especie(
            self.entrada1.fecha_entrada, self.entrada1.especie).count(), 2)

        self.assertEqual(EntradaBivalvosDepuracion.objects.filter_by_date(self.entrada1.fecha_entrada).count(),3)

    def test_entrada_biv_lotes(self):
        print('Entrada 1: ', self.entrada1.lote, 'Entrada 2: ',self.entrada2.lote)
        print(NOW.date().strftime('%y%m%d'))
        self.assertEqual(self.entrada1.lote, LOTE_DATE+'COCLCR001')
        self.assertEqual(self.entrada2.lote, LOTE_DATE+'CLJLCR001')
        self.assertEqual(self.entrada3.lote, LOTE_DATE+'COCLCR002')
