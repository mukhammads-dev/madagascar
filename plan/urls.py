from django.urls import path
from . import views

# Plan url
urlpatterns = [
    path("", views.get_home, name="get home")
]
