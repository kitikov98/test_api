from celery import Celery, shared_task
from celery.schedules import crontab
from django.core.mail import EmailMessage

timezone = 'Europe/Moscow'
app = Celery('tasks', broker='pyamqp://guest@localhost//')


@shared_task
def send_email(user_name, email_adr, user_balance):
    mail_subject = 'Your balance'
    message = 'Hello,{0} ,your last balance was : {1}'.format(user_name, user_balance)
    email = EmailMessage(mail_subject, message, to=[email_adr])
    email.send()

CELERYBEAT_SCHEDULE = {
    'context': {
        'task': 'tasks.update_number',
        'schedule': crontab(hour=7, minute=30),
    }
}

