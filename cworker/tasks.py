from celery import shared_task


@shared_task
def task1(*args, **kwargs):
    print("Hello from celery worker task 1")
    print(args[0] if args else "no args")
    return {"status": "ok", "message": "task1"}


@shared_task
def task2(*args, **kwargs):
    print("Hello from celery worker task2")
    print(args[0] if args else "no args")
    return {"status": "ok", "message": "task2"}


@shared_task
def task3(*args, **kwargs):
    print("Hello from celery worker task3")
    print(args[0] if args else "no args")
    return {"status": "ok", "message": "task3"}
