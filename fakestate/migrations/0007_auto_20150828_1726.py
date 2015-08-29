# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fakestate', '0006_auto_20150828_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='immagine',
            field=models.ImageField(default='', upload_to='uploads/'),
        ),
    ]
