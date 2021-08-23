from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
import uuid

# Create your views here.
class RegistrationAPIView(generics.GenericAPIView):

    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        # serializer.is_valid(raise_exception = True)
        # serializer.save()
        if(serializer.is_valid()):
            serializer.save()
            return Response({
                "RequestId": str(uuid.uuid4()),
                "Message": "User created successfully",
                
                "User": serializer.data}, status=status.HTTP_201_CREATED
                )
        
        return Response({"Errors": serializers.errors}, status=status.HTTP_400_BAD_REQUEST)


class ListCategoria(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = []

class DetailCategoria(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = []


class ListProducto(generics.CreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = []

class DetailProducto(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = []


class ListProveedor(generics.CreateAPIView):
    queryset = Proveedor.objects.all()
    serializer_class =  ProveedorSerializer
    permission_classes = []

class DetailProveedor(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proveedor.objects.all()
    serializer_class =  ProveedorSerializer
    permission_classes = []

class ListCarrito(generics.CreateAPIView):
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer
    permission_classes = []

class DetailCarrito(generics.RetrieveUpdateDestroyAPIView):
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer
    permission_classes = []

class ListDetalleCarrito(generics.CreateAPIView):
    queryset = DetalleCarrito.objects.all()
    serializer_class = DetalleCarritoSerializer
    permission_classes = []

class DetailDetalleCarrito(generics.RetrieveUpdateDestroyAPIView):
    queryset = DetalleCarrito.objects.all()
    serializer_class = DetalleCarritoSerializer
    permission_classes = []

class ListCompra (generics.CreateAPIView):
    queryset= Compra.objects.all()
    serializer_class=CompraSerializar
    permission_classes=[]


class DetailCompra(generics.RetrieveUpdateDestroyAPIView):
    queryset= Compra.objects.all()
    serializer_class=CompraSerializar
    permission_classes=[]

class ListUsuario (generics.CreateAPIView):
    queryset= Usuario.objects.all()
    serializer_class=UsuarioSerializer
    permission_classes=[]


class DetailUsuario(generics.RetrieveUpdateDestroyAPIView):
    queryset= Usuario.objects.all()
    serializer_class=UsuarioSerializer
    permission_classes=[]

class ListPago (generics.CreateAPIView):
    queryset= Pago.objects.all()
    serializer_class=PagoSerializar
    permission_classes=[]


class DetailPago(generics.RetrieveUpdateDestroyAPIView):
    queryset= Pago.objects.all()
    serializer_class=PagoSerializar
    permission_classes=[]

class ListVenta (generics.CreateAPIView):
    queryset= Venta.objects.all()
    serializer_class=VentaSerializer
    permission_classes=[]


class DetailVenta(generics.RetrieveUpdateDestroyAPIView):
    queryset= Venta.objects.all()
    serializer_class=VentaSerializer
    permission_classes=[]


