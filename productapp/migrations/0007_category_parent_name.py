# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0006_auto_20150629_1025'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='parent_name',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
