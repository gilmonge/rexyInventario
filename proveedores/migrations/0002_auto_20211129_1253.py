# Generated by Django 3.2.9 on 2021-11-29 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedores',
            name='direccion',
            field=models.CharField(max_length=155, verbose_name='Dirección del proveedor'),
        ),
        migrations.AlterField(
            model_name='proveedores',
            name='email',
            field=models.CharField(max_length=155, verbose_name='Correo electrónico'),
        ),
        migrations.AlterField(
            model_name='proveedores',
            name='identificacion',
            field=models.BigIntegerField(default=0, verbose_name='Número de identificación'),
        ),
    ]