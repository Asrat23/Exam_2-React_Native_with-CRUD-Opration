# Create your views here.
from django.shortcuts import render
from .models import student
from .serializers import studentserializers
from rest_framework import generics
   # student
class studlist(generics.ListCreateAPIView):
    queryset=student.objects.all()
    serializer_class=studentserializers
class studupdate(generics.RetrieveUpdateDestroyAPIView):
    queryset=student.objects.all()
    serializer_class=studentserializers


