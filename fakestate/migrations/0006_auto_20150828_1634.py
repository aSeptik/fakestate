# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fakestate', '0005_auto_20150828_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='id',
        ),
        migrations.RemoveField(
            model_name='items',
            name='item',
        ),
        migrations.AddField(
            model_name='items',
            name='item_id',
            field=models.AutoField(serialize=False, default=1, primary_key=True),
            preserve_default=False,
        ),
    ]
