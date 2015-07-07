# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0003_auto_20150624_0919'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='pathp',
            field=models.CharField(default=0, max_length=500),
            preserve_default=False,
        ),
    ]
