from celery.canvas import chain, group
from celery.result import AsyncResult
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render
from django.views import View

from cworker.tasks import (
    task1,
    task2,
    task3,
    task_priority_1,
    task_priority_5,
    task_priority_9,
)


class TestGrouping(View):
    def get(self, request: HttpRequest):
        task_group: group = group([task1.s(), task2.s()])  # type: ignore
        task_group.apply_async()
        return JsonResponse({"message": task_group.__str__()})


class TestChaining(View):
    def get(self, request: HttpRequest):
        task_chain = chain([task1.s(), task2.s(), task3.s()])  # type: ignore
        task_chain.apply_async()
        return JsonResponse({"message": task_chain.__str__()})


class TestRateLimit(View):
    def get(self, request: HttpRequest):
        task_group = group([task1.s() for i in range(10)])  # type: ignore
        task_group.apply_async()
        return JsonResponse({"message": task_group.__str__()})


class TestPriority(View):
    def get(self, request: HttpRequest):

        task_priority_5.apply_async(priority=5)  # type: ignore
        task_priority_1.apply_async(priority=1)  # type: ignore
        task_priority_9.apply_async(priority=9)  # type: ignore
        task_priority_9.apply_async(priority=9)  # type: ignore
        task_priority_1.apply_async(priority=1)  # type: ignore
        task_priority_5.apply_async(priority=5)  # type: ignore
        task_priority_1.apply_async(priority=1)  # type: ignore
        task_priority_5.apply_async(priority=5)  # type: ignore
        task_priority_9.apply_async(priority=9)  # type: ignore
        task_priority_9.apply_async(priority=9)  # type: ignore
        task_priority_5.apply_async(priority=5)  # type: ignore
        task_priority_1.apply_async(priority=1)  # type: ignore
        return JsonResponse({"message": "testing tasks priority triggered"})
