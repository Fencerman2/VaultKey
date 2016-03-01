# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_auto_20160208_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='subject_text',
            field=models.CharField(default=datetime.datetime(2016, 3, 1, 20, 31, 23, 891905, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='name_text',
            field=models.CharField(max_length=150),
        ),
    ]
