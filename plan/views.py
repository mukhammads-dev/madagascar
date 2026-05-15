from django.http import HttpResponseServerError
from django.shortcuts import render
from plan.models import Plan
plan = Plan()

# Plan controller[VIEW]


def get_home(request):
    try:
        print("\n get_home")
        # Plan Model > data
        plan.get_home()
        return render(request, "home.html", {}, status=200)

    except Exception as err:
        print("Error in get_home:", err)
        return HttpResponseServerError("Something went wrong")
