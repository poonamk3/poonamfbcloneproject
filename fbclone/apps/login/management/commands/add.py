from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Delete requirements.txt Data .'
    def add_arguments(self, parser):
        parser.add_argument('poll_ids',type=int)
    def handle(self, *args, **options):
        # self.stdout.write("Hello")
        number=options.get('poll_ids')
        # print(f"hello Welcome {poll_ids}")
        print(number)
