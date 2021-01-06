from django.views.generic import ListView, CreateView, DeleteView, DetailView
from django.urls import reverse_lazy

from .models import Patient
from users.mixins import InternMixin, DoctorMixin


class PatientListView(InternMixin, ListView):
    template_name = "patients/list.html"
    model = Patient


class PatientDeleteView(DoctorMixin, DeleteView):
    template_name = "patients/confirm_delete.html"
    model = Patient
    success_url = reverse_lazy("patient_list")


class PatientCreateView(DoctorMixin, CreateView):
    template_name = "patients/create.html"
    model = Patient
    fields = "__all__"
    success_url = reverse_lazy("patient_list")
