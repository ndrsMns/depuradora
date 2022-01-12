from django.test import TestCase
from .models import Especies

class BaseModelTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.especie = Especies.objects.create(
            fao='coc', 
            n_cientifico= 'Cerastoderma edule', 
            n_comercial='Berberecho', 
            depuracion=True)


class EspecieTest(BaseModelTestCase):
    def test_especie_format(self):
        self.assertEqual(self.especie.fao, 'COC')
    
    def test_especie_create(self):
        self.assertEqual(self.especie.fao, 'COC')
        self.assertEqual(self.especie.n_cientifico, 'Cerastoderma edule')
        self.assertEqual(self.especie.n_comercial, 'Berberecho')
        self.assertEqual(self.especie.depuracion, True)
    
    def test_especie_str(self):
        self.assertEqual(str(self.especie), 'Berberecho') 

