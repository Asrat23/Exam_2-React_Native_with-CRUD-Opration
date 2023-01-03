from django.shortcuts import render
from rest_framework import generics
from .serializers import teacherserializers
from .models import teacher

# Create your views here.
      # teacher
class teachlist(generics.ListCreateAPIView):
    queryset=teacher.objects.all()
    serializer_class=teacherserializers
class teachupdate(generics.RetrieveUpdateDestroyAPIView):
      queryset=teacher.objects.all()
      serializer_class=teacherserializers
    