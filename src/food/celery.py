from __future__ import absolute_import
import os

from django.conf import settings

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'food.settings')

app = Celery('food_app')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
