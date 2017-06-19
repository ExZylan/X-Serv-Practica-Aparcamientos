# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0006_auto_20170619_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parking',
            name='latitud',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='parking',
            name='longitud',
            field=models.CharField(max_length=256),
        ),
    ]
