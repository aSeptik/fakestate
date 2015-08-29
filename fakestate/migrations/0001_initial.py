# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('contratto', models.CharField(max_length=5, choices=[('1', 'Contratto'), ('2', 'Affitto')], default='1')),
                ('categoria', models.CharField(max_length=5, choices=[('1', 'Residenziale'), ('2', 'Commerciale'), ('3', 'Nuove costruzioni'), ('4', 'Turistico')], default='1')),
                ('tipologia', models.CharField(max_length=5, choices=[('1', 'altro'), ('2', 'appartamento'), ('3', 'attico'), ('4', 'box'), ('5', 'casa indipendente'), ('6', 'loft/open space'), ('7', 'multiproprieta'), ('8', 'palazzo/stabile'), ('9', 'rustico/casale'), ('10', 'villa'), ('11', 'villetta a schiera')], default='1')),
                ('comune', models.CharField(max_length=5, choices=[('1', 'Abbateggio'), ('2', 'Alba Adriatica'), ('3', 'Bucchianico'), ('4', 'Cannes'), ('5', 'Caramanico Terme'), ('6', 'Cepagatti'), ('7', 'Chieti'), ('8', 'Cugnoli'), ('9', 'Francavilla Al Mare'), ('10', 'Lama Dei Peligni'), ('11', 'Manoppello'), ('12', 'Montesilvano'), ('13', 'Pescara'), ('14', 'Pianella'), ('15', 'Popoli'), ('16', 'Pretoro'), ('17', 'Rosciano'), ('18', 'San Giovanni Teatino'), ('19', 'Spoltore')], default='1')),
                ('prezzo', models.DecimalField(max_digits=5, decimal_places=2)),
                ('superficie', models.BigIntegerField()),
                ('locali', models.IntegerField()),
                ('riscaldamento', models.CharField(max_length=5, choices=[('1', 'Assente'), ('2', 'Autonomo'), ('3', 'Centralizzato')], default='1')),
                ('stato', models.CharField(max_length=5, choices=[('1', 'qualsiasi'), ('2', 'Buono/Abitabile'), ('3', 'Da Ristrutturare'), ('4', 'Nuovo/In Costruzione'), ('5', 'Ottimo/Ristrutturato')], default='1')),
                ('box_auto', models.CharField(max_length=5, choices=[('1', 'si, singolo'), ('2', 'si, doppio'), ('3', 'posto auto'), ('4', 'no')], default='1')),
                ('bagni', models.CharField(max_length=5, choices=[('0', 'nessuno'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '>3')], default='1')),
                ('immagine', models.ImageField(upload_to='')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('item_id', models.ForeignKey(to='fakestate.Items')),
            ],
        ),
    ]
