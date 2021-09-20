from django.test import TestCase
from django.test.client import Client
from Carrito.models import *
from django.contrib.auth.models import User
import json

class CarritoTestCase(TestCase):
    def setUp(self) -> None:
        self.browser = Client()
        self.client = User.objects.create(username="tomastest",
                                          email='tomastest@gmail.com',
                                          password='tomastest123',
                                          first_name='tomas',
                                          last_name='alvarez',
                                          is_active=True)
        self.client.set_password("tomastest123")
        self.client.save()

        self.categoria1 = Categoria.objects.create(nombre='Tecnologia')

        self.producto1 = Producto.objects.create(nombre='Mouse',
                                                descripcion='Es un mouse de bolita',
                                                precio=10,
                                                categoria=self.categoria1)

        self.producto2 = Producto.objects.create(nombre='Teclado',
                                                descripcion='Es un teclado mecanico',
                                                precio=20,
                                                categoria=self.categoria1)
        
        self.proveedor = Proveedor.objects.create(nombre='Ricardo')

        self.compra_producto1 = Compra.objects.create(
                                                    proveedor = self.proveedor,
                                                    producto = self.producto1,
                                                    cantidad = 10,
                                                    precioCompra = 8)

        self.compra_producto2 = Compra.objects.create(
                                                    proveedor = self.proveedor,
                                                    producto = self.producto2,
                                                    cantidad = 20,
                                                    precioCompra = 10)                                            

        self.carrito = Carrito.objects.create(usuario=self.client,estado=0)
        
        self.det_carrito1 = DetalleCarrito(carrito = self.carrito, 
                                        producto = self.producto1,
                                        cantidad = 1,
                                        precioVenta = 12
                                        )

        self.det_carrito1 = DetalleCarrito(carrito = self.carrito, 
                                        producto = self.producto2,
                                        cantidad = 2,
                                        precioVenta = 200
                                        )

        response = self.browser.post('/login/', {'email': 'tomastest@gmail.com','username':'tomastest', 'password': 'tomastest123'})
        responde_js = json.loads(response.content)
        self.browser.defaults['HTTP_AUTHORIZATION'] ='Bearer {}'.format(responde_js.get('access'))

    def test_nuevo_carrito(self):
        cart = Carrito.objects.filter(usuario=self.client).last()
        print(cart.total)

        self.assertEqual(self.carrito.total,0)
        self.assertEqual(self.carrito.get_estado(),"En proceso")
        # self.assertEqual(self.carrito.get_estado(),"Cerrado")
                        
    def test_stock_prod(self):
        self.assertEqual(self.producto1.stock,10)
        self.assertEqual(self.producto2.stock,20)

    # def test_stock_prod_carrito(self):
    #     self.carrito.estado=1
    #     self.carrito.save()
        # self.producto1 = Producto.objects.create(nombre='Mouse',
        #                                         descripcion='Es un mouse de bolita',
        #                                         precio=10,
        #                                         categoria=self.categoria1)

        # self.producto2 = Producto.objects.create(nombre='Teclado',
        #                                         descripcion='Es un teclado mecanico de Switches Silent Red',
        #                                         precio=20,
        #                                         categoria=self.categoria1)
        # self.assertEqual(self.producto1.stock,9)
        # self.assertEqual(self.producto2.stock,18)