from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.serializers import ItemSerializers
from . models import ItemModel
from rest_framework import status
# Create your views here.
@api_view(['GET'])
def itemlist(request):
    item = ItemModel.objects.all()
    serializer = ItemSerializers(item,many = True)
    return Response(serializer.data)

@api_view(['POST'])
def createItem(request):
    serializer = ItemSerializers(data=request.data)
    if serializer.is_valid() :
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    
    