# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('article_name', models.CharField(max_length=200)),
                ('article_text', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name=b'date submitted')),
            ],
        ),
    ]
