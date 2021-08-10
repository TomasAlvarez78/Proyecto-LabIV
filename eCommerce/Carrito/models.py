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
    idProducto      = models.BigIntegerField(primary_key=True,null=False)
    nombre          = models.CharField(null=False,max_length=50)
    descripcion     = models.CharField(null=False,max_length=300)
    precio          = models.FloatField()
    cantidadStock   = models.FloatField()
    idCategoria     = models.ForeignKey(Categoria,on_delete=models.CASCADE,verbose_name='Categoria')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name='Producto'
        verbose_name_plural='Productos'



class DetalleCompra(models.Model):
    idProducto      = models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad        = models.IntegerField()
    precioCompra    = models.FloatField()

    class Meta:
        verbose_name='DetalleCompra'
        verbose_name_plural='DetalleCompras'



class Proveedor(models.Model):
    idProveedor     = models.BigIntegerField(primary_key=True, null=False)
    nombre          = models.CharField(null=False, max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name='Proveedor'
        verbose_name_plural='Proveedores'



class Compra(models.Model):
    idCompra        = models.BigIntegerField(primary_key=True, null=False)
    idProveedor     = models.ForeignKey(Producto,on_delete=models.CASCADE)
    idDetalleCompra = models.ForeignKey(DetalleCompra,on_delete=models.CASCADE)

    class Meta:
        verbose_name='Compra'
        verbose_name_plural='Compras'



class Usuario(models.Model):
    idUsuario       = models.BigIntegerField(primary_key=True, null=False)
    nombreUsuario   = models.CharField(null=False, max_length=50)
    contrasenia     = models.CharField(null=False, max_length=50)
    email           = models.CharField(null=False, max_length=50)
    telefono        = models.IntegerField(null=False, max_length=20)
    nombre          = models.CharField(null=False, max_length=50)
    apellido        = models.CharField(null=False, max_length=50)
    direccion       = models.CharField(null=False, max_length=50)

    def __str__(self):
        txt = "{0},{1}"
        return txt.format(self.apellido,self.nombre)

    class Meta:
        verbose_name='Usuario'
        verbose_name_plural='Usuarios'



class Carrito(models.Model):
    idCarrito       = models.BigIntegerField(primary_key=True, null=False)
    idUsuario       = models.ForeignKey(Usuario,on_delete=models.CASCADE)

    class Meta:
        verbose_name='Carrito'
        verbose_name_plural='Carritos'



class DetalleCarrito(models.Model):
    idCarrito       = models.ForeignKey(Carrito,on_delete=models.CASCADE, primary_key=True)
    idProducto      = models.ForeignKey(Producto,on_delete=models.CASCADE, primary_key=True)
    cantidad        = models.IntegerField()
    precioVenta     = models.FloatField()

    class Meta:
        verbose_name='DetalleCarrito'
        verbose_name_plural='DetalleCarritos'



class Pago(models.Model):
    idPago          = models.BigIntegerField(primary_key=True, null=False)
    idCarrito       = models.ForeignKey(Carrito,on_delete=models.CASCADE, primary_key=True)
    modoPago        = models.CharField(null=False, max_length=20)

    class Meta:
        verbose_name='Pago'
        verbose_name_plural='Pagos'



class Venta(models.Model):
    idVenta         = models.BigIntegerField(primary_key=True, null=False)
    idPago          = models.ForeignKey(Carrito,on_delete=models.CASCADE, primary_key=True)
    modoEnvio       = models.CharField(null=False, max_length=20)
    precioVenta     = models.FloatField()
    descripcion     = models.CharField(null=False, max_length=50)
    
    class Meta:
        verbose_name='Venta'
        verbose_name_plural='Ventas'


#Probando 3 2 1







