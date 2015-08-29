# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fakestate', '0003_auto_20150828_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='locali',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='items',
            name='prezzo',
            field=models.DecimalField(default=0, max_digits=6, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='items',
            name='superficie',
            field=models.BigIntegerField(default=0),
        ),
    ]
