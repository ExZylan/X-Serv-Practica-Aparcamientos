# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aparcamientos', '0010_auto_20170622_1036'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users_Page',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('titulo', models.TextField(null=True, max_length=256)),
                ('color', models.CharField(null=True, max_length=256)),
                ('background', models.CharField(null=True, max_length=256)),
                ('font_size', models.IntegerField(null=True)),
                ('usuario', models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='usuario')),
            ],
        ),
        migrations.RemoveField(
            model_name='user_page',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='User_Page',
        ),
    ]
