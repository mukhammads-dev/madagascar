from django.urls import path
from . import views

# Plan url
urlpatterns = [
    # Traditional API
    path("", views.get_home, name="get home"),
    path("create_goal", views.create_goal, name="create_goal"),
    # Rest API
    path("create_plan", views.create_plan, name="create_plan"),
    path("update_plan", views.update_plan, name="update_plan"),
    path("delete_plan", views.delete_plan, name="delete_plan"),
]
