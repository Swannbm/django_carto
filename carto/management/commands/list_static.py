from django.core.management.base import BaseCommand, CommandError
from django.contrib.staticfiles.finders import AppDirectoriesFinder, FileSystemFinder


class Command(BaseCommand):
    help = 'Localise all the Point of Interest with a specified address'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        a = AppDirectoriesFinder()
        f = FileSystemFinder()
        print(f'Found installed apps : {a.apps}')
        print('Static localisations :')
        for key, dirs in a.storages.items():
            print(f'{key} ==> {dirs._location}')
        for key, dirs in f.storages.items():
            print(f'{key} ==> {dirs._location}')
