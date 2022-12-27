from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
class Command(BaseCommand):
    help = 'Delete requirements.txt Data .'
    def handle(self, *args, **kwargs):
    	user=User.objects.all().values()
    	print(user)
        # self.stdout.write(user)

       
