from django.db import models
from django.contrib.gis.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class CampingSpot(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    location = models.PointField(srid=4326)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def lat_lon(self):
        return list(getattr(self.location, 'coords', [])[::-1])

    def __str__(self):
        return self.title
    