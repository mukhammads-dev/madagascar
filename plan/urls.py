from django.urls import path
from . import views

# Plan url
urlpatterns = [
    # Traditional API
    path("", views.get_home, name="get home"),
    path("create_goal", views.create_goal, name="create_goal"),
]
