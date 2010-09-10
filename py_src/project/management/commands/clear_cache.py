from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        from django.core.cache import cache
        cache.clear()
        print 'Done'