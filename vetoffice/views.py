from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def home(request):
    context = {"name": "Spot"}
    return render(request, "home.html", context)
