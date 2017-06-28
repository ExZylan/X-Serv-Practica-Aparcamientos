# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0015_auto_20170627_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='users_page',
            name='n_visitas',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='comment',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 28, 14, 23, 25, 225893, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='users_favs',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 28, 14, 23, 25, 225041, tzinfo=utc)),
        ),
    ]
