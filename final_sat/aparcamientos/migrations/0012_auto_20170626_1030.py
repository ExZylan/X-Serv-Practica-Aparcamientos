# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aparcamientos', '0011_auto_20170622_1043'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users_Favs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('fecha', models.DateTimeField(default=datetime.datetime(2017, 6, 26, 10, 30, 10, 457422, tzinfo=utc))),
                ('id_entidad', models.ForeignKey(to='aparcamientos.Parking')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='users_page',
            name='background',
            field=models.CharField(default='#8FE7D5', max_length=256),
        ),
        migrations.AlterField(
            model_name='users_page',
            name='color',
            field=models.CharField(default='#040E4C', max_length=256),
        ),
        migrations.AlterField(
            model_name='users_page',
            name='font_size',
            field=models.IntegerField(default=15),
        ),
    ]
