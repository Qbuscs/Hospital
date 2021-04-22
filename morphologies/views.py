from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from users.mixins import DoctorMixin, InternMixin

from .models import Morphology
from hospital.mixins import OrderableMixin, SearchableMixin, CSVMixin


class MorphologyCreateView(DoctorMixin, CreateView):
    template_name = "create.html"
    model = Morphology
    fields = "__all__"
    success_url = reverse_lazy("morphology_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["operation"] = "create"
        return context


class MorphologyUpdateView(DoctorMixin, UpdateView):
    template_name = "create.html"
    model = Morphology
    fields = "__all__"
    success_url = reverse_lazy("morphology_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["operation"] = "edit"
        return context


class MorphologyListView(InternMixin, OrderableMixin, SearchableMixin, CSVMixin, ListView):
    template_name = "list.html"
    model = Morphology
    search_fields = [("name", "icontains"), ("unit", "icontains")]


class MorphologyDeleteView(DoctorMixin, DeleteView):
    template_name = "confirm_delete.html"
    model = Morphology
    success_url = reverse_lazy("morphology_list")
