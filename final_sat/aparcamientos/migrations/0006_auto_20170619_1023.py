# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0005_remove_parking_id_entidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='parking',
            name='id_entidad',
            field=models.CharField(default=0, max_length=256),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='parking',
            name='accesibilidad',
            field=models.CharField(max_length=256),
        ),
    ]
