import os
import time

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'service.settings')

app = Celery('service')
app.config_from_object('django.conf:settings')

# Установка параметра broker_connection_retry_on_startup в True
app.conf.broker_connection_retry_on_startup = True

app.conf.broker_url = settings.CELERY_BROKER_URL
app.autodiscover_tasks()


@app.task()
def debug_task():
    time.sleep(20)
    print('Hello from debug_task')


# docker-compose run --rm web-app sh -c "python manage.py shell"
# from celery_app import debug_task
