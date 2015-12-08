# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0002_auto_20151208_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='alter_type',
            field=models.CharField(default=datetime.datetime(2015, 12, 8, 20, 36, 49, 895623, tzinfo=utc), max_length=30, choices=[(b'FLessBasic', b'Frameless Basic Land ($7)'), (b'Part', b'Partial/Pop Up ($15)'), (b'FABasic', b'Full Art Basic Land Extension ($15)'), (b'FrLess', b'Frameless($20)'), (b'FrLessSwapSimp', b'Frameless Art Swap - Simple ($30)'), (b'FrLessSwapComp', b'Frameless Art Swap - Complex ($40)'), (b'FA', b'Full Art Extension ($35)'), (b'Custom', b'Custom Full Art Swap ($45+)')]),
            preserve_default=False,
        ),
    ]
