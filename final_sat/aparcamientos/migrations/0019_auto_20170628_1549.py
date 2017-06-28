# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0018_auto_20170628_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 28, 15, 49, 59, 388390, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='users_favs',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 28, 15, 49, 59, 387989, tzinfo=utc)),
        ),
    ]
