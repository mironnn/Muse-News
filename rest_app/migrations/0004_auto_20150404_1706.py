# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rest_app', '0003_auto_20150404_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.DateField(default=datetime.datetime.now, editable=False, blank=True),
            preserve_default=True,
        ),
    ]
