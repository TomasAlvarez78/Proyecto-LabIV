from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets,status,permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .permissions import DefaultPermissions

# Create your views here.
class PermissionCategory(permissions.BasePermission):
    def has_permission(self, request, view):

        if request.method in permissions.SAFE_METHODS:
            return True

        return False

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

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

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
    # permission_classes = [permissions.IsAuthenticated]
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
        print("jejejjejejej")
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
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = []

class DetallesCarritoViewSet(viewsets.ModelViewSet):

    serializer_class = DetalleCarritoSerializer
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = []

    def get_queryset(self):
        carrito_specs = DetalleCarrito.objects.all()
        return carrito_specs

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = []
