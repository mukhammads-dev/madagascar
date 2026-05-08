from django.urls import path
from . import views
# Tour url
urlpatterns = [
    path("", views.get_tours, name="get_tours")
]
