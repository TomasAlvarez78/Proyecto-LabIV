from django.db import models
from django.db.models import Sum
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token



class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self) -> str:
        return super().__str__()

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=300)
    precio = models.FloatField()
    cantidadStock = models.FloatField()
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return super().__str__()

   

class DetalleCompra(models.Model):
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precioCompra = models.FloatField()

    def __str__(self) -> str:
        return super().__str__()

class Proveedor(models.Model):
    nombre = models.CharField  (max_length=50)

    def __str__(self) -> str:
        return super().__str__()

    
class Compra(models.Model):
    proveedor = models.ForeignKey(Proveedor,on_delete=models.CASCADE)
    detalleCompra = models.ForeignKey(DetalleCompra,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return super().__str__()

class Usuario(models.Model):
    nombreUsuario = models.CharField( max_length=50)
    contrasenia = models.CharField( max_length=50)
    email = models.CharField( max_length=50)
    telefono = models.IntegerField()
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)

    def __str__(self) -> str:
        return super().__str__()

   
        

class Carrito(models.Model):
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return super().__str__()

class DetalleCarrito(models.Model):
    carrito = models.ForeignKey(Carrito,on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad  = models.IntegerField()
    precioVenta = models.FloatField()
    
    def __str__(self) -> str:
        return super().__str__()
    

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
