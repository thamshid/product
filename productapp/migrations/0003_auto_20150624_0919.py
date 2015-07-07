# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0002_auto_20150624_0706'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cat_id', models.BigIntegerField(unique=True)),
                ('cat_name', models.CharField(max_length=30)),
                ('parent', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment_id', models.BigIntegerField(unique=True)),
                ('username', models.CharField(max_length=30)),
                ('comment_discription', models.CharField(max_length=500)),
                ('product_id', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_id', models.BigIntegerField(unique=True)),
                ('product_name', models.CharField(max_length=30)),
                ('product_cat', models.CharField(max_length=300)),
            ],
        ),
        migrations.AlterField(
            model_name='login_info',
            name='usertype',
            field=models.CharField(default=b'user', max_length=30),
        ),
    ]
