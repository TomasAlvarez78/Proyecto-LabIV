from django.contrib import admin
from Carrito.models import *
#from models import Categoria
# Register your models here.

admin.site.register(Categoria)
admin.site.register(Producto)

admin.site.register(Carrito)
admin.site.register(DetalleCarrito)

admin.site.register(Compra)
admin.site.register(Proveedor)