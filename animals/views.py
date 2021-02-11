from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView
from users.mixins import DoctorMixin, InternMixin

from .models import Animal


class AnimalCreateView(DoctorMixin, CreateView):
    template_name = "animals/create.html"
    model = Animal
    fields = ["name"]
    success_url = reverse_lazy("animal_list")


class AnimalListView(InternMixin, ListView):
    template_name = "animals/list.html"
    model = Animal


class AnimalDeleteView(DoctorMixin, DeleteView):
    template_name = "animals/confirm_delete.html"
    model = Animal
    success_url = reverse_lazy("animal_list")

