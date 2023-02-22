from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Owner, Patient
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

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


class OwnerList(ListView):
    model = Owner
    template_name = "owner_list.html"


class PatientList(ListView):
    model = Patient
    template_name = "patient_list.html"


class OwnerCreate(CreateView):
    model = Owner
    template_name = "owner_create_form.html"
    fields = ["first_name", "last_name", "phone"]
    success_url = "/owner/list"


class PatientCreate(CreateView):
    model = Patient
    template_name = "patient_create_form.html"
    fields = ["animal_type", "breed", "pet_name", "age", "owner"]
    success_url = "patient/list"


class OwnerUpdate(UpdateView):
    model = Owner
    template_name = "owner_update_form.html"
    fields = ["first_name", "last_name", "phone"]
    success_url = "/owner/list"


class PatientUpdate(UpdateView):
    model = Patient
    template_name = "patient_update_form.html"
    fields = ["animal_type", "breed", "pet_name", "age", "owner"]
    success_url = "patient/list"


class OwnerDelete(DeleteView):
    model = Owner
    template_name = "owner_delete_form.html"
    success_url = "/owner/list"


class PatientDelete(DeleteView):
    model = Patient
    template_name = "patient_delete_form.html"
    success_url = "patient/list"
