from django.db import models
from django.db.models import Sum
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=300)
    precio = models.FloatField()
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.nombre

    @property
    def stock(self):
        stockCompra = self.compras.aggregate(sum=Sum("cantidad")).get("sum",0)
        stockCompra = 0 if not stockCompra else stockCompra
        stockVenta = self.ventas.filter(carrito__estado=1).aggregate(sum=Sum("cantidad")).get("sum",0)
        stockVenta = 0 if not stockVenta else stockVenta
        print ("Prod: {} ===>  stockCompra: {}\n stockVenta: {}".format(self.nombre, stockCompra, stockVenta))
        return stockCompra - stockVenta

    class Meta:
        verbose_name='Producto'
        verbose_name_plural='Productos'

class Proveedor(models.Model):
    nombre = models.CharField  (max_length=50)

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        verbose_name='Proveedor'
        verbose_name_plural='Proveedores'
    
class Compra(models.Model):
    proveedor = models.ForeignKey(Proveedor,on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE,related_name='compras')
    cantidad = models.IntegerField(default=0)
    precioCompra = models.FloatField(default=0)

    def __str__(self) -> str:
        return f"Compra al proveedor {self.proveedor}"

    class Meta:
        verbose_name='Compra'
        verbose_name_plural='Compras'
    
# 0 - Proceso -> No resta Stock
# 1 - Vendido -> Resta Stock
# 2 - Cancelado -> No resta Stock
class Carrito(models.Model):
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    estado = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"Carrito de {self.usuario}"

    @property
    def total(self):
        total = 0
        for itemCarrito in DetalleCarrito.objects.filter(carrito=self):
            total += itemCarrito.precioVenta * itemCarrito.cantidad
        return total

class DetalleCarrito(models.Model):
    carrito = models.ForeignKey(Carrito,on_delete=models.CASCADE,related_name='dcarrito')
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE,related_name='ventas')
    cantidad  = models.IntegerField(default=0)
    precioVenta = models.FloatField(default=0)
    
    def __str__(self) -> str:
        return f"{self.producto} del Carrito de {self.carrito.usuario}"

class Pago(models.Model):
    carrito = models.ForeignKey(Carrito,on_delete=models.CASCADE)
    modoPago = models.CharField( max_length=20)
    
    def __str__(self) -> str:
        return super().__str__()

class Venta(models.Model):
    pago = models.ForeignKey(Carrito,on_delete=models.CASCADE)
    modoEnvio = models.CharField( max_length=20)
    precioVenta = models.FloatField()
    descripcion = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return super().__str__()
