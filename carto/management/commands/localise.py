from django.core.management.base import BaseCommand, CommandError
from carto.models import PointOfInterest as POI
from mapbox import Geocoder
from django.conf import settings
import traceback


class Command(BaseCommand):
    help = 'Localise all the Point of Interest with a specified address'

    def add_arguments(self, parser):
        parser.add_argument(
            '--pk',
            type=int,
            dest='pk',
            help='localise only one POI',
        )
        parser.add_argument(
            '--all',
            action='store_true',
            dest='all',
            help='localise only one POI',
        )

    def do_localisation(self, poi):
        print(f'> {poi.title:<.45}')
        try:
            print(f'> {poi.address}')
            response = self.geocoder.forward(poi.address)
            poi.geojson_response = response.geojson()
            if response.status_code != 200:
                return
            f = response.geojson()['features']
            if len(f) > 0:
                f = f[0]
                poi.localise(
                    f['center'][0],
                    f['center'][1],
                    f['place_name'],
                )
                print(f'> {poi.addresse_localised}')
                x, y = poi.get_coord()
                print(f'... ({x}, {y}) ... OK')
        except Exception as e:
            print('......ERROR')
            traceback.print_exc()
            print()

    def handle(self, *args, **options):
        self.geocoder = Geocoder(access_token=settings.MAPBOX['access_token'])
        if options['all']:
            todo = POI.objects.filter(is_localised=False)
            todo = todo.exclude(address='')
            limit = 50
            print(f'Limit to {limit} poi(s)')
            todo = todo[:limit]
            for poi in todo:
                self.do_localisation(poi)
        elif options['pk']:
            poi = POI.objects.get(pk=options['pk'])
            self.do_localisation(poi)
        else:
            print('Either --pk [integer] or --all must be provided as arguments')
