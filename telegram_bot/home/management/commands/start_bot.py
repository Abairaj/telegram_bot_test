from django.core.management.base import BaseCommand
from bot import main


class Command(BaseCommand):
    help = 'Start bot'

    def handle(self, *args, **options):
        main()  