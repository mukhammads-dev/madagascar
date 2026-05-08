from django.http import HttpResponseServerError
from django.shortcuts import render

# Tour controller[VIEW]


def get_tours(request):
    try:
        print("\n get_tours")
        return render(request, "tour.html", {}, status=200)
    except Exception as err:
        print("Error in get_tours:", err)
        return HttpResponseServerError("Something went wrong")
