from django.db.models import fields
from Carrito.models import *
from rest_framework import serializers

class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = ("id",
                  "nombre")

class ProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Producto
        fields = ("id",
                  "nombre",   
                  "precio",        
                 "cantidadStock",
                  "categoria") 
class DetalleCompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleCompra
        fields = (  "id",
                    "producto",              
                    "precioCompra")
class ProveedorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Proveedor
        fields = (  "id",
                    "nombre")

class CompraSerializar(serializers.ModelSerializer):
    class Meta:
        model= Compra
        fields= ("id",
        "proveedor",
        "detalleCompra")

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model=Usuario
        fields=("id",
        "nombreUsuario",  
        "contrasenia",    
        "email",          
        "telefono",        
        "apellido" ,       
        "direccion")

class CarritoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Carrito
        fields = ("id",
                  "usuario")

class DetalleCarritoSerializer(serializers.ModelSerializer):

    class Meta:
        model = DetalleCarrito
        fields = ("id",
                  "carrito",
                  "producto",
                  "cantidad",
                  "precioventa")
        

class PagoSerializar(serializers.ModelSerializer):
    class Meta: 
        model=Venta
        fields=("id","carrito","modopago")

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Venta
        fields= ("id","pago","modoenvio","precioventa","descripcion")

