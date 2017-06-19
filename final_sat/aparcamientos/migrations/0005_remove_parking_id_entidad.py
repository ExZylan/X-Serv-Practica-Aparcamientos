# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0004_auto_20170619_1012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parking',
            name='id_entidad',
        ),
    ]
