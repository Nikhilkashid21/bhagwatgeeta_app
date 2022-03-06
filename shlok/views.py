from django.shortcuts import render
from rest_framework import generics
from shlok.models import Shlok
from shlok.serializers import shlokSerializer

# Create your views here.
class ShlokList(generics.ListAPIView):
    queryset = Shlok.objects.all()
    serializer_class =shlokSerializer
