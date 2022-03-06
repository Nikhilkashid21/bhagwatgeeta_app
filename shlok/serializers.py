from dataclasses import fields
from turtle import title
from rest_framework import serializers
from shlok.models import Shlok

class shlokSerializer(serializers.ModelSerializer):
    class Meta:
        model=Shlok
        fields= ['id','title','shlok','meaning']