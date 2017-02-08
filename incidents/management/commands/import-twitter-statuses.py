from django.core.management.base import BaseCommand
from incidents.models import TwitterStatus


class Command(BaseCommand):
    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('screen_name', nargs='+', type=str)

    def handle(self, *args, **options):
        screen_name = options['screen_name'][0]
        print('Importing Twitter statuses…')

        





