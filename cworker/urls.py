from django.urls import URLPattern, path

import cworker.views as views

urlpatterns: list[URLPattern] = [
    path("/test-grouping", views.TestGrouping.as_view()),
    path("/test-chaining", views.TestChaining.as_view()),
]
