from django.shortcuts import render
from rest_framework import generics
from shlok.models import Adhyay, Shlok
from shlok.serializers import shlokSerializer,adhyaySerializer

# Create your views here.
class ShlokList(generics.ListAPIView):
   
    serializer_class =shlokSerializer

    def get_queryset(self):
        return Shlok.objects.filter(adhyay=self.kwargs['pk'])
    

class AdhyayList(generics.ListAPIView):
    queryset = Adhyay.objects.all()
    serializer_class =adhyaySerializer
