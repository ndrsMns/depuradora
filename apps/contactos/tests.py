from django.test import TestCase

from .models import Empresa, Contacto, Proveedor


class BaseModelTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        super(BaseModelTestCase, cls).setUpClass()

        cls.empresa = Empresa.objects.create(
            denominacion='Depuradora',
            calle='Corcubion',
            cliente=True,
            proveedor=True,
            nif='B70583539',
            rgsea='rgsea',
            codigo='LCR',
            proveedor_aprobado=True)
        cls.contacto = Contacto.objects.create(
            empresa=cls.empresa,
            nombre='Pepe',
            email='pepe@pepito.com',
            tfno='+34000000000')
        cls.proveedor = Proveedor.objects.create(
            denominacion='Depuradora',
            calle='Corcubion',
            cliente=True,
            proveedor=True,
            nif='B00000000',
            rgsea='rgsea',
            codigo='LCC',
            proveedor_aprobado=True)


class EmpresaModelTestCase(BaseModelTestCase):
    def test_empresa_created(self):
        self.assertEqual(self.empresa.denominacion, 'Depuradora')
        self.assertEqual(self.empresa.calle, 'Corcubion')
        self.assertEqual(self.empresa.nif, 'B70583539')
        self.assertEqual(self.empresa.cliente, True)
        self.assertEqual(self.empresa.proveedor, True)

    def test_empresa_str(self):
        self.assertEqual(str(self.empresa), 'Depuradora')


class ContactoModelTestCase(BaseModelTestCase):
    def test_contacto_created(self):
        self.assertEqual(str(self.contacto.empresa.denominacion), 'Depuradora')
        self.assertEqual(self.contacto.nombre, 'Pepe')
        self.assertEqual(self.contacto.email, 'pepe@pepito.com')
        self.assertEqual(self.contacto.tfno, '+34000000000')
        self.assertEqual(self.contacto.empresa.calle, 'Corcubion')

    def test_contacto_str(self):
        self.assertEqual(str(self.contacto), str(
            self.contacto.nombre) + " " + str(self.empresa))


class ProveedorModelTestCase(BaseModelTestCase):
    def test_proveedor_created(self):
        print('Número de proveedores ', len(
            Proveedor.objects.proveedor_marisco()))
        self.assertEqual(self.proveedor.denominacion, 'Depuradora')
        self.assertEqual(self.proveedor.calle, 'Corcubion')
        self.assertEqual(self.proveedor.nif, 'B00000000')
        self.assertEqual(self.proveedor.cliente, True)
        self.assertEqual(self.proveedor.proveedor, True)
