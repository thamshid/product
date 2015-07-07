# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0007_category_parent_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_discription',
            field=models.CharField(max_length=5000),
        ),
    ]
