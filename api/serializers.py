from rest_framework import serializers
from .models import UserProfile

class InsightSerializer(serializers.Serializer):
    study = serializers.CharField(max_length=255)
    hobby = serializers.CharField(max_length=255)
    job = serializers.CharField(max_length=255)
    skill = serializers.CharField(max_length=255)

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['study', 'hobby', 'skill', 'job']
