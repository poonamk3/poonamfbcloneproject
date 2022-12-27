from django.dispatch import Signal,receiver
from django.db.models.signals import post_save , pre_save
from django.dispatch import receiver
from django.core.signals import request_finished
from .models import Post , Profile
from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User

providing_args = ["title"]
notification=Signal(providing_args)

# Home Page singnal
@receiver(notification)
def show_notification(sender,**kwargs):
	print(sender)
	print(f'{kwargs}')



# Request Finished
@receiver(request_finished)
def func(sender,**kwargs):
    print("Request finishedd")


# Post Save 
def save_post(sender,instance,**kwargs):
	print("Post Save")
	print(sender)

post_save.connect(save_post,sender=Post)

def loggin_success(sender, user, request, **kwargs):
    print("loggin signal")
    print(f"user:{user}")
    print(user.password)
    print(user.email)
    print(sender)
    print(f'{kwargs}')

user_logged_in.connect(loggin_success,sender=User)

def logout(sender, user, request, **kwargs):
    print("logout signal")
    # print("user":user)
    # print("user password":user.password)
    print(sender)
    print(f'{kwargs}')

user_logged_out.connect(logout,sender=User)

@receiver(user_login_failed)
def loginfailed(sender,credentials, request, **kwargs):
    print("loginfailed signal")
    # print("user":user)
    # print("user password":user.password)
    print(sender)
    print(f'{kwargs}')



# login,logout,loginfailed,pre_save,post_save,
# pre_delete,post_delete,pre_init,post_init

@receiver(post_save,sender=User)
def prof(sender ,instance ,created ,**kwargs):
    if created:
        Profile.objects.create(user=instance)