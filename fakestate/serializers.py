from .models import Items 
from rest_framework import serializers


class ItemsSerializer(serializers.HyperlinkedModelSerializer):
 
    class Meta:
        model = Items
        fields = ('item_id', 'title', 'prezzo', 'comune', 'pub_date', 'contratto', 'categoria', 'immagine')