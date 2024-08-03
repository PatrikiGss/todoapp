# accounts/serializers.py
from rest_framework import serializers# type: ignore
from django.contrib.auth.models import User# type: ignore
from .models import UserProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

