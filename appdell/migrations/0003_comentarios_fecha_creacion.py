# Generated by Django 4.0.1 on 2022-03-23 20:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appdell', '0002_comentarios_alter_producto_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentarios',
            name='fecha_creacion',
            field=models.DateField(default=datetime.date.today),
        ),
    ]