# Generated by Django 4.0.1 on 2022-02-24 17:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('costo', models.FloatField()),
                ('descripcion_corta', models.CharField(max_length=100)),
                ('imagen', models.ImageField(null=True, upload_to='productos')),
                ('fecha_creacion', models.DateField(default=datetime.date.today)),
                ('disponible', models.BooleanField(default=True)),
                ('cantidad', models.IntegerField(default=100)),
                ('enlace', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('costo', models.FloatField(default=0.0)),
                ('fecha_creacion', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
