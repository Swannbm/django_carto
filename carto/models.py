from django.db import models
from django.conf import settings
from mapbox import Geocoder
from django.utils import timezone


class PointOfInterest(models.Model):

    class FailedLocalisation(BaseException):
        def __init__(self, response):
            msg = f'Status code: {response.status_code}, url: {response.url}'
            super().__init__(msg)
            self.response = response

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

    def localise(self):
        geocoder = Geocoder(access_token=settings.MAPBOX['access_token'])
        self.response = geocoder.forward(self.address)
        self.geojson_response = self.response.geojson()
        if self.response.status_code == 200:
            try:
                f = self.geojson_response['features']
                if len(f) > 0:
                    f = f[0]
                    self.addresse_localised = f['place_name']
                    self.longitude = f['center'][0]
                    self.latitude = f['center'][1]
                    self.is_localised = True
                    self.date_localised = timezone.now()
                    return (self.longitude, self.latitude)
                return 'Not localised, no answer'
            except:
                return f'Error, id={self.id}'
        else:
            raise PointOfInterest.FailedLocalisation(self.response)

    def __str__(self):
        return self.title
