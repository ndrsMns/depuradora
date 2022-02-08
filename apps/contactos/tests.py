from django.test import TestCase

from .models import Empresa, Contacto, Proveedor


class BaseModelTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        super(BaseModelTestCase, cls).setUpClass()

        cls.empresa = Empresa.objects.create(
            denominacion='Empresa',
            calle='Corcubion',
            cliente=True,
            proveedor=False,
            nif='B70583539',
            rgsea='rgsea',
            codigo='LCR',
            proveedor_aprobado=False)
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
            proveedor_aprobado=False)
        cls.proveedor_marisco = Proveedor.objects.create(
            denominacion='Depuradora2',
            calle='Corcubion',
            cliente=False,
            proveedor=True,
            nif='A00000000',
            rgsea='rgsea',
            codigo='LCA',
            proveedor_aprobado=True)


class EmpresaModelTestCase(BaseModelTestCase):
    def test_empresa_created(self):
        self.assertEqual(self.empresa.denominacion, 'Empresa')
        self.assertEqual(self.empresa.calle, 'Corcubion')
        self.assertEqual(self.empresa.nif, 'B70583539')
        self.assertEqual(self.empresa.cliente, True)
        self.assertEqual(self.empresa.proveedor, False)

    def test_empresa_str(self):
        self.assertEqual(str(self.empresa), 'Empresa')


class ContactoModelTestCase(BaseModelTestCase):
    def test_contacto_created(self):
        self.assertEqual(str(self.contacto.empresa.denominacion), 'Empresa')
        self.assertEqual(self.contacto.nombre, 'Pepe')
        self.assertEqual(self.contacto.email, 'pepe@pepito.com')
        self.assertEqual(self.contacto.tfno, '+34000000000')
        self.assertEqual(self.contacto.empresa.calle, 'Corcubion')

    def test_contacto_str(self):
        self.assertEqual(str(self.contacto), str(
            self.contacto.nombre) + " " + str(self.empresa))


class ProveedorModelTestCase(BaseModelTestCase):
    def test_proveedor_created(self):
        self.assertEqual(self.proveedor.denominacion, 'Depuradora')
        self.assertEqual(self.proveedor.calle, 'Corcubion')
        self.assertEqual(self.proveedor.nif, 'B00000000')
        self.assertEqual(self.proveedor.cliente, True)
        self.assertEqual(self.proveedor.proveedor, True)

    def test_proveedor_manager(self):
        print('1 : ', Proveedor.objects.first().denominacion)
        print('2 : ', Proveedor.objects.proveedor_marisco_filter().first().denominacion)
        print('3 : ', Proveedor.objects.proveedor_marisco_filter().last().denominacion)
        print('4 : ', Proveedor.objects.get(denominacion='Depuradora2'))
        print('Numero de proveedores', len(
            Proveedor.objects.proveedor_filter()))
        print('Numero de proveedores de marisco', len(
            Proveedor.objects.proveedor_marisco_filter()))
        self.assertEqual(
            len(Proveedor.objects.proveedor_filter()),
            2)
        self.assertEqual(
            len(Proveedor.objects.proveedor_marisco_filter()),
            1)
