from rest_framework import serializers
from .models import KitabPost

class KitabPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = KitabPost
        fields = ["id", "title", "content", "published_date"]
