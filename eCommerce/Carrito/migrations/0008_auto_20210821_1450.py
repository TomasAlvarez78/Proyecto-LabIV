# Generated by Django 3.2.5 on 2021-08-21 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Carrito', '0007_venta'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carrito',
            options={},
        ),
        migrations.AlterModelOptions(
            name='categoria',
            options={},
        ),
        migrations.AlterModelOptions(
            name='compra',
            options={},
        ),
        migrations.AlterModelOptions(
            name='detallecarrito',
            options={},
        ),
        migrations.AlterModelOptions(
            name='detallecompra',
            options={},
        ),
        migrations.AlterModelOptions(
            name='pago',
            options={},
        ),
        migrations.AlterModelOptions(
            name='producto',
            options={},
        ),
        migrations.AlterModelOptions(
            name='proveedor',
            options={},
        ),
        migrations.AlterModelOptions(
            name='usuario',
            options={},
        ),
        migrations.AlterModelOptions(
            name='venta',
            options={},
        ),
        migrations.AlterField(
            model_name='compra',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Carrito.proveedor'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Carrito.categoria'),
        ),
    ]