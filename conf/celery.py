import os
from datetime import timedelta

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django-celery.settings")

app = Celery("django-celery")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    "run-every-10-seconds": {
        "task": "django-celery.tasks.foo",
        "schedule": timedelta(seconds=10),
    },
    "run-every-1800-seconds": {
        "task": "django-celery.tasks.bar",
        "schedule": timedelta(seconds=1800),
    },
}
