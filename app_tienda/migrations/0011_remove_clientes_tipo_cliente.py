# Generated by Django 5.1.3 on 2024-12-08 04:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_tienda', '0010_alter_vendedores_telefono'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientes',
            name='tipo_cliente',
        ),
    ]
