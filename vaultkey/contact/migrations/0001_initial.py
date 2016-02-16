# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_text', models.CharField(max_length=100)),
                ('email_text', models.CharField(max_length=200)),
                ('message_text', models.TextField()),
            ],
        ),
    ]
