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
        print("STEP 2: FRONTENDdan BACKENDga kirib kelish")

        plans = plan.get_home()

        print("STEP 5: BACKENDdan FRONTENDga javob yuborish")
        return render(request, "home.html", {"plans": plans}, status=200)

    except Exception as err:
        print("Error in get_home:", err)
        return HttpResponseServerError("Something went wrong")

  # Creat with Traditional API


@csrf_exempt
def create_goal(request):
    try:
        print("\n create_goal")
        print("STEP 2 create: FRONTENDdan BACKENDga kirib kelish")
        if request.method != "POST":
            raise ValueError("Only post requests are allowed")

        content = request.POST.get("content")
        print("STEP 5 create: BACKENDdan FRONTENDga javob yuborish")
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
        print("STEP2: Backend recieved API Request")
        if request.method != "POST":
            raise ValueError("Only post requests are allowed")

        data = json.loads(request.body)
        print("request.body:", data)

        result = plan.create_plan(data)  # call
        print("STEP5: Backend > API Response > Frontend")
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
