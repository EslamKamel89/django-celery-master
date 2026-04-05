from django.urls import URLPattern, path

import cworker.views as views

urlpatterns: list[URLPattern] = [
    path("/test-grouping", views.TestGrouping.as_view()),
    path("/test-chaining", views.TestChaining.as_view()),
    path("/test-rate-limit", views.TestRateLimit.as_view()),
    path("/test-task-priority", views.TestPriority.as_view()),
]
