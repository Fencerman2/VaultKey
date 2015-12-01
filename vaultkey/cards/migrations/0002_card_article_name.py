# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='article_name',
            field=models.CharField(default=datetime.datetime(2015, 12, 1, 20, 41, 26, 477595, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
