from django.core.management.base import BaseCommand
from django.conf import settings
from carto.models import PointOfInterest as POI
from mapbox import Geocoder


class Command(BaseCommand):
    help = 'Localise POI according to ID'

    def add_arguments(self, parser):
        parser.add_argument('id', nargs='+', type=int)

    def handle(self, *args, **options):
        geocoder = Geocoder(access_token=settings.MAPBOX['access_token'])
        for id in options['id']:
            poi = POI.objects.get(pk=id)
            rep = geocoder.forward(poi.address)
            if rep.status_code == 200:
                geojson = rep.geojson()
                try:
                    f = geojson['features'][0]
                    poi.place = f['place_name']
                    poi.longitude = f['center'][0]
                    poi.latitude = f['center'][1]
                except:
                    print(geojson)