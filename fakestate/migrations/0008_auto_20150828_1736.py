# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fakestate', '0007_auto_20150828_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='immagine',
            field=models.ImageField(upload_to='uploads/', default='uploads/no_image_thumb.gif'),
        ),
    ]
