from typing import List
from django.urls import path
from Carrito.views import *

urlpatterns =[
    path('categoria', ListCategoria.as_view(), name='categoria'),
    path('categories/<int:pk>/', DetailCategoria.as_view(), name='singlecategoria'),
    
    path('Carrito', ListCarrito.as_view(), name='carrito'),
    path('carrito/<int:pk>/', DetailCarrito.as_view(), name='singlecarrito'),

    path('detallecarrito', ListDetalleCarrito.as_view(), name='detallecarrito'),
    path('detallecarrito/<int:pk>/', DetailDetalleCarrito.as_view(), name='singledetallecarrito'),

    path('producto', ListProducto.as_view(), name='producto'),
    path('producto/<int:pk>/', DetailProducto.as_view(), name='singleproducto'),
    
    path('proveedor', ListProveedor.as_view(), name='proveedor'),
    path('proveedor/<int:pk>/', DetailProveedor.as_view(), name='singleproveedor'),

    path('usuario', ListUsuario.as_view(), name='usuario'),
    path('usuario/<int:pk>/', DetailUsuario.as_view(), name='singleusuario'),

    path('pago', ListPago.as_view(), name='pago'),
    path('pago/<int:pk>/', DetailPago.as_view(), name='singlepago'),
    
    path('venta', ListVenta.as_view(), name='venta'),
    path('venta/<int:pk>/', DetailVenta.as_view(), name='singleventa'),

    path('compra', ListCompra.as_view(), name='compra'),
    path('venta/<int:pk>/', DetailCompra.as_view(), name='singlecompra'),



]
