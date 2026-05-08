from django.urls import path
from . import views
# Sport url
urlpatterns = [
    path("", views.get_sports, name="get_sports")
]
