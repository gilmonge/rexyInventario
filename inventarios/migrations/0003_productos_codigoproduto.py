# Generated by Django 3.2.9 on 2021-11-24 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventarios', '0002_rename_inventarios_productos'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='codigoProduto',
            field=models.CharField(default='0', max_length=50, verbose_name='Código del producto'),
        ),
    ]
