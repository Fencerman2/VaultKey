# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0005_remove_request_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='alter_type',
            field=models.CharField(max_length=30, choices=[(b'FLessBasic', b'Frameless Basic Land ($7)'), (b'Part', b'Partial/Pop Up ($15)'), (b'FABasic', b'Full Art Basic Land Extension ($15)'), (b'FrLess', b'Frameless ($20)'), (b'FrLessSwapSimp', b'Frameless Art Swap - Simple ($30)'), (b'FrLessSwapComp', b'Frameless Art Swap - Complex ($40)'), (b'FA', b'Full Art Extension ($35)'), (b'Custom', b'Custom Full Art Swap ($45+)')]),
        ),
    ]
