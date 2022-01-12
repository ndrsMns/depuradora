from django.test import TestCase

from .models import Piscinas, Zonas


class BaseModelTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        super(BaseModelTestCase, cls).setUpClass()

        cls.zona = Zonas.objects.create(nombre_zona='depuradora', ubicacion='Corcubion')
        cls.piscina = Piscinas.objects.create(zona = cls.zona, no_piscina ='Piscina1')


class ZonaModelTestCase(BaseModelTestCase):
    def test_zona_created(self):
        self.assertEqual(self.zona.nombre_zona, 'depuradora')
        self.assertEqual(self.zona.ubicacion, 'Corcubion')

    def test_zona_str(self):
        self.assertEqual(str(self.zona), 'depuradora')

class PiscinaModelTestCase(BaseModelTestCase):
    def test_piscina_created(self):
        self.assertEqual(str(self.piscina.zona), 'depuradora')
        self.assertEqual(self.piscina.no_piscina, 'Piscina1')
        
    def test_piscina_str(self):
        self.assertEqual(str(self.piscina), 'Piscina1') 

