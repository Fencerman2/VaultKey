# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_auto_20160301_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email_text',
            field=models.CharField(max_length=200, verbose_name=b'Email Address'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message_text',
            field=models.TextField(verbose_name=b'Message'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name_text',
            field=models.CharField(max_length=150, verbose_name=b'Name'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='subject_text',
            field=models.CharField(max_length=200, verbose_name=b'Subject'),
        ),
    ]
