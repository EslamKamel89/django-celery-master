from typing import cast

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
    test_passing_arguments,
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


class TestPassingArguments(View):
    def get(self, request: HttpRequest):
        result = cast(AsyncResult, test_passing_arguments.apply_async(args=["Eslam", 37]))  # type: ignore
        test_passing_arguments.apply_async(kwargs={"name": "Ahmed", "age": 66})  # type: ignore
        # the get method is blocking and it will block the execution until the result is available
        print("get = ", result.get())
        print("id = ", result.id)
        print("status = ", result.status)
        print("result = ", result.result)
        print("ready = ", result.ready())
        print("successful = ", result.successful())
        print("failed = ", result.failed())
        return JsonResponse({"message": "test_passing_arguments is triggered"})
