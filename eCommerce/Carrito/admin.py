from django.contrib import admin
from Carrito.models import *
#from models import Categoria
# Register your models here.

admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(DetalleCompra)
admin.site.register(Proveedor)

admin.site.register(Carrito)
admin.site.register(Usuario)