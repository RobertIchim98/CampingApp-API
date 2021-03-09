from rest_framework import serializers

from .models import CampingSpot

class CampingSpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampingSpot
        lat_lon = serializers.Field()
        fields = (
            'id','title', 'description', 'location', 'timestamp', 'owner', 'lat_lon'
        )