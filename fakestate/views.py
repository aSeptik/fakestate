from django.shortcuts import render
from .serializers import ItemsSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Items


def index(request):
    items = Items.objects.all()  # //order_by('-pub_date')[:5]
    return render(request, 'fakestate/index.html', {'latest_item_list': items})


#http://www.django-rest-framework.org/tutorial/2-requests-and-responses/
@api_view(['GET'])
def ItemsList(request,  format=None):

    if request.method == 'GET':

        items = Items.objects.all()
        serializer = ItemsSerializer(items, many=True)
        return Response(serializer.data)

@api_view(['GET'])	
def SingleItem(request, pk):
    try:
        item = Items.objects.get(pk=pk)
    except item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ItemsSerializer(item)
        return Response(serializer.data)

			
 
