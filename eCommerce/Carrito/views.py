from django.db.models.query_utils import Q
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets,status,permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .permissions import DefaultPermissions,CarritoPermissions
# list -> GET
# retrieve -> GET con /1 (id)
# create -> POST
# destroy -> DELETE
# update  -> PUT
# partial-update -> PATCH

class CategoriaViewSet(viewsets.ModelViewSet, DefaultPermissions):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    # authentication_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [DefaultPermissions]

    # def list(self, request):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     page = self.paginate_queryset(queryset)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)

    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        if request.user.is_superuser:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response("No tiene permisos suficientes", status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        if request.user.is_superuser:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response("No tiene permisos suficientes", status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        if request.user.is_superuser:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            if getattr(instance, '_prefetched_objects_cache', None):
                instance._prefetched_objects_cache = {}

            return Response(serializer.data)
        return Response("No tiene permisos suficientes", status=status.HTTP_400_BAD_REQUEST)

class ProductoViewSet(viewsets.ModelViewSet):

    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [DefaultPermissions]

    def create(self, request, *args, **kwargs):
        if request.user.is_superuser:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response("No tiene permisos suficientes", status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        if request.user.is_superuser:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response("No tiene permisos suficientes", status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        if request.user.is_superuser:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            if getattr(instance, '_prefetched_objects_cache', None):
                instance._prefetched_objects_cache = {}

            return Response(serializer.data)
        return Response("No tiene permisos suficientes", status=status.HTTP_400_BAD_REQUEST)

class CarritoViewSet(viewsets.ModelViewSet):

    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer
    permission_classes = [CarritoPermissions]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Carrito.objects.all()
        return Carrito.objects.filter(usuario=user)

    def create(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            created = Carrito.objects.create(usuario=user)
            created.save()
            return Response("Nuevo carrito creado", status=status.HTTP_201_CREATED)
        return Response("No es un cliente autenticado", status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            carts = Carrito.objects.filter(usuario=user)
            if carts:
                last_cart = carts.last()
            if last_cart.estado == 0:
                Carrito.objects.filter(pk=last_cart.id).update(estado=1)
                return Response("Se cerro el ultimo carrito", status=status.HTTP_202_ACCEPTED)
            else:
                return Response("Este carrito ya ha sido cerrado", status=status.HTTP_400_BAD_REQUEST)        
        return Response("No es un cliente autenticado", status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response("No es un cliente autenticado", status=status.HTTP_400_BAD_REQUEST)


class DetallesCarritoViewSet(viewsets.ModelViewSet):
    queryset = DetalleCarrito.objects.all()
    serializer_class = DetalleCarritoSerializer
    permission_classes = [CarritoPermissions]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return DetalleCarrito.objects.all()
        last_cart = Carrito.objects.filter(usuario=user).last()
        if last_cart:
            return DetalleCarrito.objects.filter(carrito=last_cart)
        return self.queryset.none()

    def create(self, request, *args, **kwargs):
        user = request.user
        # Si no tiene carrito que devuelva mensaje
        if user.is_authenticated:
            producto = request.data['producto']
            cantidad = request.data['cantidad']
            precioVenta = request.data['precioVenta']

            itemfilter = Producto.objects.get(id=producto)
            if (itemfilter.stock >= cantidad):
                last_cart = Carrito.objects.filter(usuario=user.id).last()
                item, created = DetalleCarrito.objects.get_or_create(producto=itemfilter,carrito=last_cart)
                if item:
                    item.cantidad += int(cantidad)
                    item.precioVenta += precioVenta
                    item.save()
                return Response(status=status.HTTP_200_OK, data=request.data)
            else:
                return Response("No hay suficiente stock de un producto", status=status.HTTP_400_BAD_REQUEST)
        return Response("No es un cliente autenticado", status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response("No es un cliente autenticado", status=status.HTTP_400_BAD_REQUEST)
