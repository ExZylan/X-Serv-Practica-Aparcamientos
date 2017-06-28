# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0019_auto_20170628_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 28, 16, 8, 28, 31790, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='users_favs',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 28, 16, 8, 28, 31362, tzinfo=utc)),
        ),
    ]
