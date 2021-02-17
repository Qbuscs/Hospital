from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from users.mixins import DoctorMixin, InternMixin

from afflictions.models import Sickness


class SicknessCreateView(DoctorMixin, CreateView):
    template_name = "sicknesses/create.html"
    model = Sickness
    fields = ["name", "afflictions"]
    success_url = reverse_lazy("sickness_list")


class SicknessUpdateView(DoctorMixin, UpdateView):
    template_name = "sicknesses/create.html"
    model = Sickness
    fields = ["name", "afflictions"]

    def get_success_url(self):
        return reverse_lazy("sickness_detail", kwargs={"pk": self.object.pk})


class SicknessListView(InternMixin, ListView):
    template_name = "sicknesses/list.html"
    model = Sickness


class SicknessDeleteView(DoctorMixin, DeleteView):
    template_name = "sicknesses/confirm_delete.html"
    model = Sickness
    success_url = reverse_lazy("sickness_list")


class SicknessDetailView(InternMixin, DetailView):
    template_name = "sicknesses/detail.html"
    model = Sickness
