from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework import authentication, permissions
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

# Create your views here.


class CategoriaViewSet(viewsets.ModelViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [permissions.IsAuthenticated]
    #permission_classes = []


class ProductoViewSet(viewsets.ModelViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [permissions.IsAuthenticated]
    #permission_classes = []

class CarritoViewSet(viewsets.ModelViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer
    permission_classes = [permissions.IsAuthenticated]
    #permission_classes = []

class DetallesCarritoViewSet(viewsets.ModelViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    queryset = DetalleCarrito.objects.all()
    serializer_class = DetalleCarritoSerializer
    permission_classes = [permissions.IsAuthenticated]
    #permission_classes = []

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = []







