from django.http import HttpResponseServerError
from django.shortcuts import render

# Plan controller[VIEW]


def get_home(request):
    try:
        print("get_home")
        # Plan Model > data
        data = "MIT"
        return render(request, "home.html", {'data': data}, status=200)
    except Exception as err:
        print("Error in get_home:", err)
        return HttpResponseServerError("Something went wrong")
