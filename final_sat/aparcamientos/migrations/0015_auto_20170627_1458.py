# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0014_auto_20170627_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='titulo',
            field=models.TextField(max_length=256, default='Sin título'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 27, 14, 58, 36, 87880, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='users_favs',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 27, 14, 58, 36, 87429, tzinfo=utc)),
        ),
    ]
