from celery.canvas import group
from celery.result import AsyncResult
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render
from django.views import View

from cworker.tasks import task1, task2


class Test(View):
    def get(self, request: HttpRequest):
        task_group: group = group([task1.s(), task2.s()])  # type: ignore
        task_group.apply_async()
        return JsonResponse({"message": task_group.__str__()})
