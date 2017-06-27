# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aparcamientos', '0013_auto_20170626_1145'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('texto', models.TextField(max_length=256)),
                ('id_entidad', models.IntegerField()),
                ('fecha', models.DateTimeField(default=datetime.datetime(2017, 6, 27, 14, 18, 7, 988460, tzinfo=utc))),
                ('autor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='users_favs',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 27, 14, 18, 7, 987641, tzinfo=utc)),
        ),
    ]
