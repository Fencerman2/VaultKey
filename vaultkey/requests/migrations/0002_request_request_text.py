# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='request_text',
            field=models.TextField(default=datetime.datetime(2015, 12, 3, 14, 46, 39, 504175, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
