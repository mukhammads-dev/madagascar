from django.http import HttpResponse, HttpResponseServerError
from django.shortcuts import render
from portfolio.data import author

# Portfolio controller[VIEW]


def get_portfolio(request):
    try:
        print("\n get_portfolio")
        # Portfolio Model > data
        return render(request, "portfolio.html", author, status=200)
    except Exception as err:
        print("Error in get_portfolio:", err)
        return HttpResponseServerError("Something went wrong")


def say_hello(request):
    try:
        print("\n say_hello")
        # Portfolio Model > data
        return HttpResponse("<h1> Author says hello </h1>")
    except Exception as err:
        print("Error in say_hello:", err)
        return HttpResponseServerError("Something went wrong")


def get_advice(request):
    try:
        print("\n get_advice")
        # Portfolio Model > data
        return HttpResponse("<h1> Lets create Portfolio </h1>")
    except Exception as err:
        print("Error in get_advice:", err)
        return HttpResponseServerError("Something went wrong")
