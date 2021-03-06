# Generated by Django 3.2.9 on 2021-12-11 17:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bodegas', '0001_initial'),
        ('inventarios', '0004_productos_categoria'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transacciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha del movimiento')),
                ('tipo', models.BooleanField(default=False, verbose_name='Tipo movimiento')),
                ('cantidad', models.IntegerField(default=0, verbose_name='Cantidad registrada')),
                ('bodega', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='bodegas.bodegas', verbose_name='Bodega')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='inventarios.productos', verbose_name='Producto')),
                ('responsable', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Quien realizó el movimiento')),
            ],
        ),
    ]
