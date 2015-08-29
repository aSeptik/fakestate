# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fakestate', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='items',
            old_name='item_id',
            new_name='item',
        ),
        migrations.AddField(
            model_name='items',
            name='title',
            field=models.CharField(max_length=250, default=datetime.datetime(2015, 8, 28, 13, 48, 30, 97200, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
