from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Delete requirements.txt Data .'
    def add_arguments(self, parser):
        parser.add_argument('poll_ids',type=int)
    def handle(self, *args, **kwargs):
        # self.stdout.write("Hello")
        f = open("requirements.txt", "w")
        f.write("Woops! I have deleted the content! poll_ids ")
        f.close()

        #open and read the file after the appending:
        f = open("requirements.txt", "r")
        print(f.read())

        print(f"hello Welcome {poll_ids}")
