from .models import student
from rest_framework import serializers


class studentserializers(serializers.ModelSerializer):
    class Meta:
        model=student
        fields='__all__'
