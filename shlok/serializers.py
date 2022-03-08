from dataclasses import fields
from rest_framework import serializers
from shlok.models import Adhyay, Shlok

class shlokSerializer(serializers.ModelSerializer):
    class Meta:
        model=Shlok
        fields= ['id','title','shlok','meaning','adhyay']

class adhyaySerializer(serializers.ModelSerializer):
    class Meta:
        model=Adhyay
        fields= ['id','title','subtitle']