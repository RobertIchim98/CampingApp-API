from django.contrib.gis import admin
from .models import CampingSpot

admin.site.register(CampingSpot, admin.OSMGeoAdmin)