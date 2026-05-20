import json
from django.http import HttpResponseServerError, JsonResponse
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

  # Creat with Traditional API


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

 # Creat with Rest API


@csrf_exempt
def create_plan(request):
    try:
        print("\n create_plan")
        if request.method != "POST":
            raise ValueError("Only post requests are allowed")

        data = json.loads(request.body)
        print("request.body:", data)

        result = plan.create_plan(data)  # call
        return JsonResponse({"status": "succes", "result": result}, status=201)

    except Exception as err:
        message = str(err)
        return JsonResponse({"status": "fail", "message": message}, status=500)


@csrf_exempt
def update_plan(request):
    try:
        print("\n update_plan")
        if request.method != "POST":
            raise ValueError("Only post requests are allowed")

        data = json.loads(request.body)
        print("request.body:", data)

        result = plan.update_plan(data)  # call
        # HTTP 201 500 200
        return JsonResponse({"status": "succes", "result": result}, status=201)

    except Exception as err:
        message = str(err)
        return JsonResponse({"status": "fail", "message": message}, status=500)


@csrf_exempt
def delete_plan(request):
    try:
        print("\n update_plan")
        if request.method != "POST":
            raise ValueError("Only post requests are allowed")

        data = json.loads(request.body)
        print("request.body:", data)

        result = plan.delete_plan(data)

        return JsonResponse({"status": "succes", "result": result}, status=201)

    except Exception as err:
        message = str(err)
        return JsonResponse({"status": "fail", "message": message}, status=500)


@csrf_exempt
def delete_all_plans(request):
    try:
        print("\n delete_all_plans")  # STEP 1 Backendga kirish
        if request.method != "POST":
            raise ValueError("Only post requests are allowed")

        result = plan.delete_all_plans()
        return JsonResponse({"status": "succes", "result": result}, status=201)

    except Exception as err:
        message = str(err)
        return JsonResponse({"status": "fail", "message": message}, status=500)
