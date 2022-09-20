from ast import Return
from urllib import response
from django.http import JsonResponse
from .models import drink
from .serializers import drinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET','POST'])
def drink_list(request,format=None):
    if request.method=='GET':
        drinks=drink.objects.all()
        serializer=drinkSerializer(drinks, many=True)
        return Response({"drinks": serializer.data})
    elif request.method=='POST':
        serializer=drinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def drink_detail(request,id,format=None):
    drinkk=drink.objects.get(pk=id)
    if request.method=='GET':
        serializer=drinkSerializer(drinkk)
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer=drinkSerializer(drinkk, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response('error')
    elif request.method=='DELETE':
        drinkk.delete()
        return Response('deleted')