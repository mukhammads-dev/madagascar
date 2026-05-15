from django.http import HttpResponseServerError
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from plan.models import Plan
plan = Plan()

# Plan controller[VIEW]

# Read API method function


def get_home(request):
    try:
        print("\n get_home")
        plans = plan.get_home()
        return render(request, "home.html", {"plans": plans}, status=200)

    except Exception as err:
        print("Error in get_home:", err)
        return HttpResponseServerError("Something went wrong")

# Create API method function


@csrf_exempt
def create_goal(request):
    try:
        print("\n create_goal")
        if request.method != "POST":
            raise ValueError("Only post requests are allowed")

        content = request.POST.get("content")
        print("content:", content)
        plan.create_goal(content)
        return redirect("/")

    except Exception as err:
        print("Error in create_goal:", err)
        return HttpResponseServerError("Creation is failed")
