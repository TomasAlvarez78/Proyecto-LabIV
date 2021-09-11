from django.db.models import fields
from Carrito.models import *
from rest_framework import serializers
from django.contrib.auth.models import User

class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = '__all__'


class ProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Producto
        fields = '__all__'

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

class CarritoSerializer(serializers.ModelSerializer):

    # dcarrito = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='dcarrito-detail'
    # )

    class Meta:
        model = Carrito
        fields = ['id','usuario']
        # fields = ['id','usuario','dcarrito']

class DetalleCarritoSerializer(serializers.ModelSerializer):

    class Meta:
        model = DetalleCarrito
        fields = ("id",
                  "carrito",
                  "producto",
                  "cantidad",
                  "precioVenta")
        

class PagoSerializar(serializers.ModelSerializer):
    class Meta: 
        model=Venta
        fields=("id","carrito","modopago")

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Venta
        fields= ("id","pago","modoenvio","precioventa","descripcion")

