from rest_framework import serializers

from .models import UrlShortener

class UrlShortenerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrlShortener
        fields = ["originUrl"]

class UrlShortenerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrlShortener
        fields = "__all__"