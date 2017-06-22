# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aparcamientos', '0008_auto_20170619_1143'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('titulo', models.TextField(max_length=256, null=True)),
                ('color', models.CharField(max_length=256, null=True)),
                ('background', models.CharField(max_length=256, null=True)),
                ('font_size', models.IntegerField(null=True)),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='style_css',
            name='usuario',
        ),
        migrations.AlterField(
            model_name='parking',
            name='accesibilidad',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='parking',
            name='contacto',
            field=models.TextField(default='NO HAY DATOS', max_length=256),
        ),
        migrations.AlterField(
            model_name='parking',
            name='id_entidad',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='parking',
            name='longitud',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='selected_parking',
            name='usuario',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Style_CSS',
        ),
    ]
