# Generated by Django 5.1.3 on 2024-12-07 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_tienda', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='clase_de_producto',
            field=models.CharField(default='default_value', max_length=30),
        ),
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(null=True),
        ),
    ]