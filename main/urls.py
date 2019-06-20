from django.urls import path
from . import views


urlpatterns = [
    path("", views.index),
    path("make_lesson", views.make_lesson)
]