# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0017_auto_20170628_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 28, 15, 44, 25, 500206, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='users_favs',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 28, 15, 44, 25, 499807, tzinfo=utc)),
        ),
    ]
