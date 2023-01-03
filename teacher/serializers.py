from .models import teacher
from rest_framework import serializers
class teacherserializers(serializers.ModelSerializer):
    class Meta:
        model=teacher
        fields='__all__'
        