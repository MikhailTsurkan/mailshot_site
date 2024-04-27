from celery import shared_task
from django.core.mail import send_mail


@shared_task
def async_send(**kwargs):
    print(*kwargs.values())
    send_mail(**kwargs)
