from rest_framework import serializers
from .models import Guidance

class GuidanceSerializer(serializers.ModelSerializer):
    favorite_count = serializers.IntegerField(source='get_favorite_count', read_only=True)

    class Meta:
        model = Guidance
        fields = ['title', 'content', 'image', 'religion', 'favorite_count']

    def get_favorite_count(self, obj) -> int:
        return obj.favorite_users.count()