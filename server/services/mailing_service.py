from django.core.mail import send_mail

from pages.models import Subscribe
from authsystem.models import User 
from server.celery import app

@app.task()
def notificate(author_id):
    subscribers = Subscribe.objects.filter(author__pk=author_id).select_related()
    for sub in  subscribers:
        send_object = send_mail(
        "New post from your favorite author!",
        f"Your author {sub.author.username} publicated new post! Check his profile!",
        "alexander.kizimenko@mail.ru",
        [str(sub.subscriber.email)],
        fail_silently=True,)
        del send_object
    return {'successful': True}