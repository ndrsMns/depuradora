from django.test import TestCase

from models import Empresa, Contacto, Proveedor


class BaseModelTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        super(BaseModelTestCase, cls).setUpClass()

        cls.empresa = Empresa.objects.create(
            denominacion='Depuradora',
            calle='Corcubion',
            cliente=True,
            proveedor=True)
        cls.contacto = Contacto.objects.create(
            empresa=cls.empresa,
            nombre='Pepe',
            email='pepe@pepito.com',
            tfno='+34000000000')
        cls.proveedor = Proveedor.objects.create(
            rgsea='rgsea',
            codigo='LCR',
            proveedor_aprobado=True)
        cls.cliente = Cliente.objects.create(
            nif='B70583539')


class EmpresaModelTestCase(BaseModelTestCase):
    def test_empresa_created(self):
        self.assertEqual(self.empresa.denominacion, 'Depuradora')
        self.assertEqual(self.empresa.calle, 'Corcubion')
        self.assertEqual(self.empresa.cliente, True)
        self.assertEqual(self.empresa.proveedor, True)

    def test_empresa_str(self):
        self.assertEqual(str(self.empresa), 'Depuradora')


class ContactoModelTestCase(BaseModelTestCase):
    def test_contacto_created(self):
        self.assertEqual(str(self.contacto.denominacion), 'Depuradora')
        self.assertEqual(self.contacto.nombre, 'Pepe')
        self.assertEqual(self.contacto.email, 'pepe@pepito.com')
        self.assertEqual(self.contacto.tfno, '+34000000000')
        self.assertEqual(self.contacto.calle, 'Corcubion')

    def test_contacto_str(self):
        self.assertEqual(str(self.contacto), str(self.contacto.nombre) + " " + str(self.empresa))

class ProveedorModelTestCase(BaseModelTestCase):
    def test_proveedor_created(self):
        self.assertEqual(str(self.proveedor.denominacion), 'Depuradora')
        self.assertEqual(str(self.proveedor.rgsea), 'rgsea')
        self.assertEqual(str(self.proveedor.codigo), 'LCR')
        self.assertEqual(str(self.proveedor.proveedor_aprobado), True)

class ClienteModelTestCase(BaseModelTestCase):
    def test_cliente_created(self):
        self.assertEqual(str(self.cliente.denominacion), 'Depuradora')
        self.assertEqual(str(self.cliente.nif), 'B70583539')

