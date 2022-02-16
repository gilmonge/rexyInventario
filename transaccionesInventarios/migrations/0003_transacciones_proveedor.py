# Generated by Django 3.2.9 on 2022-02-15 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0003_auto_20220126_2007'),
        ('transaccionesInventarios', '0002_auto_20220103_1243'),
    ]

    operations = [
        migrations.AddField(
            model_name='transacciones',
            name='proveedor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='proveedores.proveedores', verbose_name='Proveedor del inventario'),
        ),
    ]
