from django.urls import path
from . import views
# Portfolio url
urlpatterns = [
    path("", views.get_portfolio, name="get_portfolio"),
    path("say", views.say_hello, name="say_hello"),
    path("advice", views.get_advice, name="get_advice")
]
