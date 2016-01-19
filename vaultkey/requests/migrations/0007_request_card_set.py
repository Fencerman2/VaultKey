# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0006_auto_20151214_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='card_set',
            field=models.CharField(default=datetime.datetime(2016, 1, 19, 16, 55, 7, 75179, tzinfo=utc), max_length=150),
            preserve_default=False,
        ),
    ]
