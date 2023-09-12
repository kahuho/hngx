from rest_framework import serializers
from .models import StageOneData

class StageOneDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = StageOneData
        fields = '__all__'
