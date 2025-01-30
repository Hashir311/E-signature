from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("canvas/", views.canvas, name="canvas"),
    path("canvas/save/", views.save, name="save"),
    path("view_saved/", views.view_saved, name="view_saved"),
]
