from django.db import models

# Create your models here.

class Categoria(models.Model):
    idCategoria     = models.BigIntegerField(primary_key=True,null=False)
    nombre          = models.CharField(null=False,max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name='Categoria'
        verbose_name_plural='Categorias'

class Producto(models.Model):
    idProducto  = models.BigIntegerField(primary_key=True,null=False)
    nombre      = models.CharField(null=False,max_length=50)
    descripcion = models.CharField(null=False,max_length=300)
    precio      = models.FloatField()
    cantidadStock = models.FloatField()
    idCategoria     = models.ForeignKey(Categoria,on_delete=models.CASCADE,verbose_name='Categoria')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name='Producto'
        verbose_name_plural='Productos'

class DetalleCompra(models.Model):
    idProducto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precioCompra = models.FloatField()

class Proveedor(models.Model):
    idProveedor = models.BigIntegerField(primary_key=True, null=False)
    nombre = models.CharField(null=False, max_length=50)

    class Meta:
        verbose_name='Proveedor'
        verbose_name_plural='Proveedores'

#Probando 3 2 1







