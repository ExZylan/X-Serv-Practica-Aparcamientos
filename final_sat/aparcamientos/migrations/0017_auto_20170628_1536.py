# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0016_auto_20170628_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 28, 15, 36, 32, 911277, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='users_favs',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 28, 15, 36, 32, 910872, tzinfo=utc)),
        ),
    ]
