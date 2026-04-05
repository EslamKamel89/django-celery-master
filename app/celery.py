import os

from celery import Celery
from django.conf import settings
from kombu import Exchange, Queue

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
app = Celery("app")
app.config_from_object("django.conf:settings", namespace="CELERY")
# app.conf.task_routes = {
#     "cworker.tasks.task1": {"queue": "queue1"},
#     "cworker.tasks.task2": {"queue": "queue2"},
# }
# app.conf.broker_transport_options = {
#     "priority_steps": list(range(10)),
#     "sep": ":",
#     "queue_order_strategy": "priority",
# }
# app.conf.task_default_queue = "celery"
app.conf.worker_prefetch_multiplier = 1
app.conf.worker_concurrency = 1
# app.conf.task_default_rate_limit = "1/m"
app.conf.task_acks_late = True
app.conf.task_queues = [
    Queue(
        "tasks",
        exchange=Exchange("tasks", type="direct", durable=True),
        routing_key="tasks",
        durable=True,
        queue_arguments={"x-max-priority": 10},
    )
]
app.conf.task_default_priority = 5
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
