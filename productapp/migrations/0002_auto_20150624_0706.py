# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='login_info',
            old_name='userntype',
            new_name='usertype',
        ),
    ]
