# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('comentario', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Parkings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('id_entidad', models.IntegerField()),
                ('nombre', models.CharField(max_length=256)),
                ('descripcion', models.TextField()),
                ('accesibilidad', models.IntegerField()),
                ('url', models.CharField(max_length=256)),
                ('direccion', models.CharField(max_length=256)),
                ('barrio', models.CharField(max_length=256)),
                ('distrito', models.CharField(max_length=256)),
                ('latitud', models.CharField(max_length=256)),
                ('longitud', models.CharField(max_length=256)),
                ('contacto', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Selected_Parking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('fecha', models.DateField(auto_now=True)),
                ('id_entidad', models.ForeignKey(to='aparcamientos.Parkings')),
                ('usuario', models.ForeignKey(default='', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Style_CSS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('usuario', models.CharField(max_length=256)),
                ('titulo', models.CharField(max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name='comments',
            name='id_entidad',
            field=models.ForeignKey(to='aparcamientos.Parkings'),
        ),
    ]
