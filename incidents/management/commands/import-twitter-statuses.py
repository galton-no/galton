from django.core.management.base import BaseCommand
from incidents.models import TwitterStatus
import twitter
import pprint
from credentials import twitter_api as twitter_api_credentials


class Command(BaseCommand):
    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('screen_name', nargs='+', type=str)

    def handle(self, *args, **options):
        screen_name = options['screen_name'][0]
        print('Importing Twitter statuses…')

        api = twitter.Api(consumer_key=twitter_api_credentials['consumer_key'],
                          consumer_secret=twitter_api_credentials['consumer_secret'],
                          access_token_key=twitter_api_credentials['access_token_key'],
                          access_token_secret=twitter_api_credentials['access_token_secret'])

        pretty_printer = pprint.PrettyPrinter()

        statuses = api.GetUserTimeline(screen_name=screen_name)
        pretty_printer.pprint(statuses)

        for raw_status in statuses:
            status = TwitterStatus(foreign_key=str(raw_status.id))


            status.save()

            print(status.id)





