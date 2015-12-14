# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0004_auto_20151214_1608'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='pub_date',
        ),
    ]
