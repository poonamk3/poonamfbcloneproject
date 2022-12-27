from django.core.mail import send_mail
def send_mail_without():
    send_mail("No Celery Work" ,"massage_body",
        "poonamk@thoughtwin.com",
        ["poonamkumar9098@gmail.com"],
        fail_silently=False
        )
    return None
