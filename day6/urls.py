from django.urls import path
from . import views


app_name = "day6"

urlpatterns = [
    path("index/", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("created/", views.created, name="created"),
    path("detail/<int:pk>/", views.detail, name="detail"),
    path("delete/<int:pk>/", views.delete, name="delete"),
    path("edit/<int:pk>/", views.edit, name="edit"),
    path("editted/<int:pk>/", views.editted, name="editted"),
]
