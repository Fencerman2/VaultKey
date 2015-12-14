# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0003_request_alter_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='card_provided',
            field=models.BooleanField(default=datetime.datetime(2015, 12, 14, 21, 8, 13, 18597, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='request',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'date submitted'),
        ),
    ]
