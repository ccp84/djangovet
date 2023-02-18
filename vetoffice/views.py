from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

pets = [
    {"petname": "Fido", "animal_type": "dog"},
    {"petname": "Clementine", "animal_type": "cat"},
    {"petname": "Cleo", "animal_type": "cat"},
    {"petname": "Oreo", "animal_type": "dog"},
]


def home(request):
    context = {
        "name": "Dr Vet",
        "pets": pets
    }
    return render(request, "home.html", context)
