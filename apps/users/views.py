from django.shortcuts import render
from django.views.generic import View
# Create your views here.


def login(request):
    if request.method == "POST":
        pass
    elif request.method == "GET":
        return render(request, "login.html", {})

