from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from users.mixins import DoctorMixin, InternMixin

from afflictions.models import Vaccine
from hospital.mixins import OrderableMixin, SearchableMixin, CSVMixin


class VaccineCreateView(DoctorMixin, CreateView):
    template_name = "vaccine/create.html"
    model = Vaccine
    fields = ["sickness"]
    success_url = reverse_lazy("vaccine_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["operation"] = "create"
        return context


class VaccineUpdateView(DoctorMixin, UpdateView):
    template_name = "vaccine/create.html"
    model = Vaccine
    fields = ["sickness"]

    def get_success_url(self):
        return reverse_lazy("vaccine_list")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["operation"] = "edit"
        return context


class VaccineListView(InternMixin, OrderableMixin, SearchableMixin, CSVMixin, ListView):
    template_name = "vaccine/list.html"
    model = Vaccine
    paginate_by = 10
    search_fields = [("sickness__name", "icontains")]


class VaccineDeleteView(DoctorMixin, DeleteView):
    template_name = "vaccine/confirm_delete.html"
    model = Vaccine
    success_url = reverse_lazy("vaccine_list")
