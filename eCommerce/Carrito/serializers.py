from django.db.models import fields
from Carrito.models import *
from rest_framework import serializers
from django.contrib.auth.models import User

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    
    stock = serializers.SerializerMethodField()

    class Meta:
        model = Producto
        fields = '__all__'

    def get_stock(self,instance):
        return instance.stock

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = ("id","nombre")

class CompraSerializar(serializers.ModelSerializer):
    class Meta:
        model= Compra
        fields= ("id","proveedor","detalleCompra")

class CarritoSerializer(serializers.ModelSerializer):

    total = serializers.SerializerMethodField()

    dcarrito = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='Carrito:dcarrito-detail'
    )

    class Meta:
        model = Carrito
        # fields = ['id','usuario']
        fields = '__all__'
    
    def get_total(self,instance):
        return instance.total

class DetalleCarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleCarrito
        fields = ["id","carrito","producto","cantidad","precioVenta"]

#NO TOCAR POR AHORA
class PagoSerializar(serializers.ModelSerializer):
    class Meta: 
        model=Venta
        fields=("id","carrito","modopago")

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Venta
        fields= ("id","pago","modoenvio","precioventa","descripcion")

