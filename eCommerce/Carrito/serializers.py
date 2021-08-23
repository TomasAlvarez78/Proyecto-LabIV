from django.db.models import fields
from Carrito.models import *
from rest_framework import serializers
from django.contrib.auth.models import User

class RegistrationSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(max_length=50, min_length=6)
    username = serializers.CharField(max_length=50, min_length=6)
    password = serializers.CharField(max_length=150, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'username', 'password')

    def validate(self, args):
        email = args.get('email', None)
        username = args.get('username', None)
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': ('email already exists')})
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'username': ('username already exists')})

        return super().validate(args)
  

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    

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

