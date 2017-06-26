# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0012_auto_20170626_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users_favs',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 26, 11, 45, 16, 561084, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='users_favs',
            name='id_entidad',
            field=models.IntegerField(),
        ),
    ]
