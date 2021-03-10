from rest_framework import serializers

from .models import CampingSpot
from django.contrib.auth import get_user_model
User = get_user_model()

class CampingSpotSerializer(serializers.ModelSerializer):
    # use owner username instead of id
    owner = serializers.SlugRelatedField(slug_field="username", queryset=User.objects.all())


    class Meta:
        model = CampingSpot
        lat_lon = serializers.Field()
        fields = (
            'id','title', 'description', 'location', 'timestamp', 'owner', 'lat_lon'
        )