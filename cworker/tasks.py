from celery import shared_task


@shared_task
def task1():
    print("Hello from celery worker task 1")
    return {"status": "ok", "message": "task1"}


@shared_task
def task2():
    print("Hello from celery worker task2")
    return {"status": "ok", "message": "task2"}
