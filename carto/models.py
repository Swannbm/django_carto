from django.db import models
from django.conf import settings
from mapbox import Geocoder
from django.utils import timezone


class POICategory(models.Model):
    COLOR_CHOICES = (
        ('1', 'Blue'),
        ('2', 'Red'),
        ('3', 'Green'),
        ('4', 'Orange'),
        ('5', 'Yellow'),
        ('6', 'Violet'),
        ('7', 'Grey'),
        ('8', 'Black'),
    )
    label = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    color_id = models.CharField(max_length=1, 
                                choices=COLOR_CHOICES,
                                default='3')
    # poi_set = list of PointOfInterest from foreign key

    def __str__(self):
        return self.label


class PointOfInterest(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    address = models.TextField(max_length=400)
    is_localised = models.BooleanField(default=False)
    date_localised = models.DateTimeField(null=True, blank=True)
    addresse_localised = models.TextField(max_length=400, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    geojson_response = models.TextField(blank=True)
    url = models.URLField(null=True, blank=True)
    category = models.ForeignKey(POICategory,
                                 on_delete=models.PROTECT,
                                 related_name='poi_set',
                                 null=True)

    def localise(self, longitude, latitude, address):
        self.is_localised = True
        self.date_localised = timezone.now()
        self.addresse_localised = address
        self.longitude = longitude
        self.latitude = latitude
        self.save()

    def get_coord(self, reverse=False):
        if reverse == False:
            return self.longitude, self.latitude
        else:
            return self.latitude, self.longitude
    
    def __str__(self):
        return self.title



