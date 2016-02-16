# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_submit'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Submit',
            new_name='Send',
        ),
    ]
