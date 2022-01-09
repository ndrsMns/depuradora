from django.test import TestCase
from .models import Especies

class EspecieTest(TestCase):
    def test_especie_format(self):
        berbe = Especies.objects.create(
            fao='coc', 
            n_cientifico= 'Cerastoderma edule', 
            n_comercial='Berberecho', 
            depuracion=True)
        self.assertEqual(berbe.fao, 'COC')
        self.assertEqual(berbe.n_cientifico, 'Cerastoderma edule')
        self.assertEqual(berbe.n_comercial, 'Berberecho')
        self.assertEqual(berbe.depuracion, True)
    
    def test_especie_create(self):
        berbe = Especies.objects.create(
            fao='coc', 
            n_cientifico= 'Cerastoderma edule', 
            n_comercial='Berberecho', 
            depuracion=True)
        berbe2 = Especies.objects.get(fao='COC')
        self.assertEqual(berbe2.fao, 'COC')
        self.assertEqual(berbe2.n_cientifico, 'Cerastoderma edule')
        self.assertEqual(berbe2.n_comercial, 'Berberecho')
        self.assertEqual(berbe2.depuracion, True)

