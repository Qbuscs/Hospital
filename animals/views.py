from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from users.mixins import DoctorMixin, InternMixin

from .models import Animal
from hospital.mixins import OrderableMixin, SearchableMixin, CSVMixin


class AnimalCreateView(DoctorMixin, CreateView):
    template_name = "animals/create.html"
    model = Animal
    fields = ["name"]
    success_url = reverse_lazy("animal_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["operation"] = "create"
        return context


class AnimalListView(InternMixin, OrderableMixin, SearchableMixin, CSVMixin, ListView):
    template_name = "animals/list.html"
    model = Animal
    paginate_by = 10
    search_fields = [("name", "icontains")]


class AnimalDeleteView(DoctorMixin, DeleteView):
    template_name = "animals/confirm_delete.html"
    model = Animal
    success_url = reverse_lazy("animal_list")


class AnimalUpdateView(DoctorMixin, UpdateView):
    template_name = "animals/create.html"
    model = Animal
    fields = ["name"]
    success_url = reverse_lazy("animal_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["operation"] = "edit"
        return context
