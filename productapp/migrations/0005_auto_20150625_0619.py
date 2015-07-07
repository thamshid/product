# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0004_category_pathp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cat_id',
            field=models.BigIntegerField(default=0, unique=True),
        ),
    ]
