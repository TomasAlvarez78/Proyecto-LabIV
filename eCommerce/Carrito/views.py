from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .permissions import CategoryPermissions
# Create your views here.


class PermissionCategory(permissions.BasePermission):
    def has_permission(self, request, view):

        if request.method in permissions.SAFE_METHODS:
            return True

        return False


class CategoriaViewSet(viewsets.ModelViewSet, PermissionCategory):

    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    # authentication_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = []

    def get_queryset(self):
        """
        Get the list of items for this view.
        This must be an iterable, and may be a queryset.
        Defaults to using `self.queryset`.

        This method should always be used rather than accessing `self.queryset`
        directly, as `self.queryset` gets evaluated only once, and those results
        are cached for all subsequent requests.

        You may want to override this if you need to provide different
        querysets depending on the incoming request.

        (Eg. return a list of items that is specific to the user)
        """
        assert self.queryset is not None, (
            "'%s' should either include a `queryset` attribute, "
            "or override the `get_queryset()` method."
            % self.__class__.__name__
        )

        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = queryset.all()
        return queryset


class ProductoViewSet(viewsets.ModelViewSet):

    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = []


class CarritoViewSet(viewsets.ModelViewSet):

    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = []


class DetallesCarritoViewSet(viewsets.ModelViewSet):

    serializer_class = DetalleCarritoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        carrito_specs = DetalleCarrito.objects.all()
        return carrito_specs

    # permission_classes = []


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = []
