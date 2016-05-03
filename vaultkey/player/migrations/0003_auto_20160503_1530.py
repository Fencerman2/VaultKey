# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0002_player_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='player_name',
            new_name='player_firstname',
        ),
        migrations.AddField(
            model_name='player',
            name='player_lastname',
            field=models.CharField(default=datetime.datetime(2016, 5, 3, 19, 30, 42, 21408, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
