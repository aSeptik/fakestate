# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fakestate', '0004_auto_20150828_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='prezzo',
            field=models.BigIntegerField(default=0),
        ),
    ]
