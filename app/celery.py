import os

from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
app = Celery("app")
app.config_from_object("django.conf:settings", namespace="CELERY")
# app.conf.task_routes = {
#     "cworker.tasks.task1": {"queue": "queue1"},
#     "cworker.tasks.task2": {"queue": "queue2"},
# }
app.conf.broker_transport_options = {
    "priority_steps": list(range(10)),
    "sep": ":",
    "queue_order_strategy": "priority",
}
app.conf.task_default_queue = "celery"
app.conf.task_default_priority = 5
app.conf.worker_prefetch_multiplier = 1
app.conf.task_default_rate_limit = "1/m"
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
