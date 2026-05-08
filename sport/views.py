from django.http import HttpResponseServerError
from django.shortcuts import render

# Sport controller[VIEW]


def get_sports(request):
    try:
        print("\n get_sports")
        return render(request, "sport.html", {}, status=200)
    except Exception as err:
        print("Error in get_sports:", err)
        return HttpResponseServerError("Something went wrong")
