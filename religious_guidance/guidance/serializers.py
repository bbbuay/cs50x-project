from rest_framework import serializers
from .models import Guidance

class GuidanceSerializer(serializers.ModelSerializer):
    favorite_count = serializers.SerializerMethodField()

    class Meta:
        model = Guidance
        fields = ['id', 'title', 'content', 'image', 'religion', 'favorite_count']

    def get_favorite_count(self, obj) -> int:
        return obj.favorite_users.count()