from celery import shared_task
from time import sleep
from django.core.mail import send_mail


@shared_task
def sleepy(duariton):
	sleep(10)
	return None

@shared_task
def send_mail_task():
    send_mail("Celery Work" ,"massage_body",
        "poonamk@thoughtwin.com",
        ["poonamkumar9098@gmail.com"],
        fail_silently=False
        )
    print("Celery mail")
    return None


    
@shared_task
def send_mail_taskdetails():
    send_mail("details Work" ,"massage_body",
        "poonamk@thoughtwin.com",
        ["poonamkumar9098@gmail.com"],
        fail_silently=False
        )
    print("details mail")
    return None