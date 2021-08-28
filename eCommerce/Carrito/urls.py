from django.urls import path
from Carrito.views import *
from rest_framework.routers import DefaultRouter

app_name = "Carrito"

router = DefaultRouter()
router.register("categorias", CategoriaViewSet, basename="categorias")
router.register("productos", ProductoViewSet, basename="productos")
router.register("carrito", CarritoViewSet, basename="carrito")
router.register("dcarrito", DetallesCarritoViewSet, basename="dcarrito")
router.register("usuarios", UsuarioViewSet, basename="usuarios")

urlpatterns = router.urls
