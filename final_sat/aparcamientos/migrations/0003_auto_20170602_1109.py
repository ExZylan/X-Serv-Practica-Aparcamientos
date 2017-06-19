# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0002_auto_20170602_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parking',
            name='latitud',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='parking',
            name='longitud',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='selected_parking',
            name='fecha',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='style_css',
            name='usuario',
            field=models.ForeignKey(default=b'', to=settings.AUTH_USER_MODEL),
        ),
    ]
