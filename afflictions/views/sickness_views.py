from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from users.mixins import DoctorMixin, InternMixin

from afflictions.models import Sickness
from hospital.mixins import OrderableMixin, SearchableMixin


class SicknessCreateView(DoctorMixin, CreateView):
    template_name = "sicknesses/create.html"
    model = Sickness
    fields = ["name", "afflictions"]
    success_url = reverse_lazy("sickness_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["operation"] = "create"
        return context


class SicknessUpdateView(DoctorMixin, UpdateView):
    template_name = "sicknesses/create.html"
    model = Sickness
    fields = ["name", "afflictions"]

    def get_success_url(self):
        return reverse_lazy("sickness_detail", kwargs={"pk": self.object.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["operation"] = "edit"
        return context


class SicknessListView(InternMixin, OrderableMixin, SearchableMixin, ListView):
    template_name = "sicknesses/list.html"
    model = Sickness
    search_fields = ["name"]


class SicknessDeleteView(DoctorMixin, DeleteView):
    template_name = "sicknesses/confirm_delete.html"
    model = Sickness
    success_url = reverse_lazy("sickness_list")


class SicknessDetailView(InternMixin, DetailView):
    template_name = "sicknesses/detail.html"
    model = Sickness
