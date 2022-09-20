from dataclasses import field, fields
from email.mime import image
from msilib.schema import Class
from pyexpat import model
from rest_framework import serializers
from .models import drink

class drinkSerializer(serializers.ModelSerializer):
    class Meta:
        model=drink
        fields=['id','name','price','description','img']