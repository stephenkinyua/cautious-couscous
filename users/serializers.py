
from rest_framework import serializers
from djoser.serializers import TokenCreateSerializer

class CustomLoginSerializer(TokenCreateSerializer):
    phone_number = serializers.CharField()
