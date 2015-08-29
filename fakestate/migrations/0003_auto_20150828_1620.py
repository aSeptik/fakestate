# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fakestate', '0002_auto_20150828_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='immagine',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AlterField(
            model_name='items',
            name='locali',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='items',
            name='prezzo',
            field=models.DecimalField(decimal_places=2, max_digits=5, default=''),
        ),
        migrations.AlterField(
            model_name='items',
            name='superficie',
            field=models.BigIntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='items',
            name='title',
            field=models.CharField(max_length=250, default=''),
        ),
    ]
