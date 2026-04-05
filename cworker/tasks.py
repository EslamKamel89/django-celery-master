import time

from celery import shared_task


@shared_task(queue="tasks")
def task1(*args, **kwargs):
    print("Hello from celery worker task 1")
    print(args[0] if args else "no args")
    return {"status": "ok", "message": "task1"}


@shared_task(queue="tasks")
def task2(*args, **kwargs):
    print("Hello from celery worker task2")
    print(args[0] if args else "no args")
    return {"status": "ok", "message": "task2"}


@shared_task(queue="tasks")
def task3(*args, **kwargs):
    print("Hello from celery worker task3")
    print(args[0] if args else "no args")
    return {"status": "ok", "message": "task3"}


@shared_task(queue="tasks")
def task_priority_1(*args, **kwargs):
    print("Hello from celery worker task_priority_1")
    time.sleep(5)
    return {"status": "ok", "message": "task_priority_1"}


@shared_task(queue="tasks")
def task_priority_5(*args, **kwargs):
    print("Hello from celery worker task_priority_5")
    time.sleep(5)
    return {"status": "ok", "message": "task_priority_5"}


@shared_task(queue="tasks")
def task_priority_9(*args, **kwargs):
    print("Hello from celery worker task_priority_9")
    time.sleep(5)
    return {"status": "ok", "message": "task_priority_9"}
