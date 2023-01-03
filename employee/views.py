from django.shortcuts import render
from rest_framework import generics
from .serializers import employeeserializers
from .models import employee

# Create your views here.
    # employee
class emplist(generics.ListCreateAPIView):
    queryset=employee.objects.all()
    serializer_class=employeeserializers
class empupdate(generics.RetrieveUpdateDestroyAPIView):
    queryset=employee.objects.all()
    serializer_class=employeeserializers
class insert(generics.CreateAPIView):
    queryset=employee.objects.all()
    serializer_class=employeeserializers