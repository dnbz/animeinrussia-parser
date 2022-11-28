import os
from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'animeinrussia.settings')

app = Celery('animeinrussia')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# # Load task modules from all registered Django apps.
app.autodiscover_tasks(['air'])


# @app.on_after_finalize.connect
# def setup_periodic_tasks(sender, **kwargs):
#     print(air.tasks.fuck)
#     # sender.add_periodic_task(2.0, air.tasks.bruh.s())

#     # sender.add_periodic_task(1.0, fuck.s())
#     sender.add_periodic_task(1.0, air.tasks.fuck.s())
#     # # Executes every Monday morning at 7:30 a.m.
#     # sender.add_periodic_task(
#     #     crontab(hour=7, minute=30, day_of_week=1),
#     #     test.s('Happy Mondays!'),
#     # )
#     #
