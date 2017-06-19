# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0007_auto_20170619_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parking',
            name='contacto',
            field=models.TextField(),
        ),
    ]
