from django.db import models
from django.db.models import Sum
class Categoria(models.Model):
    nombre          = models.CharField(null=False,max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name='Categoria'
        verbose_name_plural='Categorias'

class Producto(models.Model):
    nombre          = models.CharField(null=False,max_length=50)
    descripcion     = models.CharField(null=False,max_length=300)
    precio          = models.FloatField()
    ##cantidadStock   = models.FloatField()
    categoria       = models.ForeignKey(Categoria,on_delete=models.CASCADE,verbose_name='Categoria')
    @property
    def stock(self):
        stockcompra = Actualiza_stock.objects.filter(product=self).aggregate(sum=Sum("monto")).get("sum")
        stockventa = DetalleCarrito.objects.filter(product=self, cart__confirmed=True).aggregate(sum=Sum("monto")).get("sum")
        if stockcompra == None:
            boughtStock = 0
        if stockventa == None:
            soldStock = 0

        print("{} stockCompra: {}, stockVenta: {}".format(self.title, boughtStock, soldStock))
        return boughtStock - soldStock
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name='Producto'
        verbose_name_plural='Productos'

class DetalleCompra(models.Model):
    producto        = models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad        = models.IntegerField()
    precioCompra    = models.FloatField()

    class Meta:
        verbose_name='DetalleCompra'
        verbose_name_plural='DetalleCompras'

class Proveedor(models.Model):
    nombre          = models.CharField(null=False, max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name='Proveedor'
        verbose_name_plural='Proveedores'

class Compra(models.Model):
    proveedor     = models.ForeignKey(Producto,on_delete=models.CASCADE)
    detalleCompra = models.ForeignKey(DetalleCompra,on_delete=models.CASCADE)

    class Meta:
        verbose_name='Compra'
        verbose_name_plural='Compras'

class Usuario(models.Model):
    nombreUsuario   = models.CharField(null=False, max_length=50)
    contrasenia     = models.CharField(null=False, max_length=50)
    email           = models.CharField(null=False, max_length=50)
    telefono        = models.IntegerField(null=False)
    nombre          = models.CharField(null=False, max_length=50)
    apellido        = models.CharField(null=False, max_length=50)
    direccion       = models.CharField(null=False, max_length=50)

    def __str__(self):
        txt = "{0} {1}"
        return txt.format(self.apellido,self.nombre)

    class Meta:
        verbose_name='Usuario'
        verbose_name_plural='Usuarios'

class Carrito(models.Model):
    usuario       = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    class Meta:
        verbose_name='Carrito'
        verbose_name_plural='Carritos'

class DetalleCarrito(models.Model):
    carrito       = models.ForeignKey(Carrito,on_delete=models.CASCADE)
    producto      = models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad        = models.IntegerField()
    precioVenta     = models.FloatField()

    class Meta:
        verbose_name='DetalleCarrito'
        verbose_name_plural='DetalleCarritos'

class Pago(models.Model):
    carrito       = models.ForeignKey(Carrito,on_delete=models.CASCADE)
    modoPago        = models.CharField(null=False, max_length=20)

    class Meta:
        verbose_name='Pago'
        verbose_name_plural='Pagos'

class Venta(models.Model):
    pago            = models.ForeignKey(Carrito,on_delete=models.CASCADE)
    modoEnvio       = models.CharField(null=False, max_length=20)
    precioVenta     = models.FloatField()
    descripcion     = models.CharField(null=False, max_length=50)
    
    class Meta:
        verbose_name='Venta'
        verbose_name_plural='Ventas'

class Actualiza_stock(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    monto = models.SmallIntegerField()
    precio = models.FloatField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}: {} ({})".format(self.producto, self.proveedor, self.monto)
