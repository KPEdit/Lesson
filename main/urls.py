from django.urls import path

from . import views


urlpatterns = [
    path("", views.index),
    path("make_lesson", views.make_lesson),
    path("make_category", views.make_category),
    path("lesson/<link>", views.lesson)
]