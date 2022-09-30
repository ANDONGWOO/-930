from django.urls import path
from . import views


app_name = "day6"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
]
