from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import Emailing

class EmailingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emailing
        fields = '__all__'