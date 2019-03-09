from django.core.management.base import BaseCommand, CommandError
from carto.models import PointOfInterest as POI

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
        poi.address = poi.address.replace('93 300', '93300')
        try:
            print(f'> {poi.address}')
            coord = poi.localise()
            poi.save()
            print(f'> {poi.addresse_localised}')
            print(f'... {coord} ... OK')
        except POI.FailedLocalisation as e:
            print('......ERROR')
            print(e.__traceback__)
        print()

    def handle(self, *args, **options):
        if options['all']:
            todo = POI.objects.filter(is_localised=False)
            todo = todo.exclude(address='')
            for poi in todo:
                self.do_localisation(poi)
        elif options['pk']:
            poi = POI.objects.get(pk=options['pk'])
            self.do_localisation(poi)
        else:
            print('Either --pk [integer] or --all must be provided as arguments')
