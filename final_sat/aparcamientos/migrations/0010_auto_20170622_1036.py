# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0009_auto_20170621_1835'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='id_entidad',
        ),
        migrations.RemoveField(
            model_name='selected_parking',
            name='id_entidad',
        ),
        migrations.RemoveField(
            model_name='selected_parking',
            name='usuario',
        ),
        migrations.AddField(
            model_name='parking',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='parking',
            name='n_comentarios',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user_page',
            name='usuario',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
        migrations.DeleteModel(
            name='Selected_Parking',
        ),
    ]
