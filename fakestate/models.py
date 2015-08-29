import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Items(models.Model):
	
	
	CONTRATTO_CHOICES = (
		('1', 'Contratto'),
		('2', 'Affitto')
	)	
	
	
	CATECORIA_CHOICES = (
		('1' , 'Residenziale'),
		('2' , 'Commerciale'),
		('3' , 'Nuove costruzioni'),
		('4' , 'Turistico' ),
	)    


	TIPOLOGIA_CHOICES = (
		('1' , 'altro'),
		('2' , 'appartamento'),
		('3' , 'attico'),
		('4' , 'box'),
		('5' , 'casa indipendente'),
		('6' , 'loft/open space'),
		('7' , 'multiproprieta'),
		('8' , 'palazzo/stabile'),
		('9' , 'rustico/casale'),
		('10' , 'villa'),
		('11' , 'villetta a schiera'),
	)    
	

	COMUNI_CHOICES = (
	  ('1' , 'Abbateggio'),
	  ('2' , 'Alba Adriatica'),
	  ('3' , 'Bucchianico'),
	  ('4' , 'Cannes'),
	  ('5' , 'Caramanico Terme'),
	  ('6' , 'Cepagatti'),
	  ('7' , 'Chieti'),
	  ('8' , 'Cugnoli'),
	  ('9' , 'Francavilla Al Mare'),
	  ('10' , 'Lama Dei Peligni'),
	  ('11' , 'Manoppello'),
	  ('12' , 'Montesilvano'),
	  ('13' , 'Pescara'),
	  ('14' , 'Pianella'),
	  ('15' , 'Popoli'),
	  ('16' , 'Pretoro'),
	  ('17' , 'Rosciano'),
	  ('18' , 'San Giovanni Teatino'),
	  ('19' , 'Spoltore'),
	)    


	STATO_CHOICES = (
		('1' , 'qualsiasi'),
		('2' , 'Buono/Abitabile'),
		('3' , 'Da Ristrutturare'),
		('4' , 'Nuovo/In Costruzione'),
		('5' , 'Ottimo/Ristrutturato'),
	)



	RISCALDAMENTO_CHOICES = (
	  ('1', 'Assente'),
	  ('2', 'Autonomo'),
	  ('3', 'Centralizzato'),
	)    

	BOXAUTO_CHOICES = (
		('1' , 'si, singolo'),
		('2' , 'si, doppio'),
		('3' , 'posto auto'),
		('4' , 'no'),
	)

	BAGNI_CHOICES = (
		('0' , 'nessuno'),
		('1' , '1'),
		('2' , '2'),
		('3' , '3'),
		('4' , '>3'),
	)
	
	item_id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=250, default='')
	contratto = models.CharField(max_length=5, choices=CONTRATTO_CHOICES, default='1')
	categoria = models.CharField(max_length=5, choices=CATECORIA_CHOICES, default='1')
	tipologia = models.CharField(max_length=5, choices=TIPOLOGIA_CHOICES, default='1')
	comune = models.CharField(max_length=5, choices=COMUNI_CHOICES, default='1')
	prezzo = models.BigIntegerField(default=0)
	superficie = models.BigIntegerField(default=0)
	locali = models.IntegerField(default=0)
	riscaldamento = models.CharField(max_length=5, choices=RISCALDAMENTO_CHOICES, default='1')
	stato = models.CharField(max_length=5, choices=STATO_CHOICES, default='1')
	box_auto = models.CharField(max_length=5, choices=BOXAUTO_CHOICES, default='1')
	bagni = models.CharField(max_length=5, choices=BAGNI_CHOICES, default='1')
	immagine = models.ImageField(upload_to='uploads/', default='uploads/no_image_thumb.gif')
	pub_date = models.DateTimeField('date published')
	
	
	def __str__(self):              # __unicode__ on Python 2
		return self.title
	
# from fakestate.models import Items
# from decimal import Decimal
# from django.utils import timezone
# Items.objects.all()
# j = Items(title="Terreno in vendita", pub_date=timezone.now(), prezzo='98000', comune='7', contratto='1', categoria='2')
# i.save()



#python manage.py makemigrations fakestate