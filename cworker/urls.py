from django.urls import URLPattern, path

import cworker.views as views

urlpatterns: list[URLPattern] = [
    path("/test", views.Test.as_view()),
]
