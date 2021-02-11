from django.views.generic import ListView, CreateView, DeleteView, DetailView
from django.urls import reverse_lazy

from .models import Patient, Examination
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


class ExaminationListView(InternMixin, ListView):
    template_name = "examinations/list.html"
    model = Examination


class ExaminationCreateView(DoctorMixin, CreateView):
    template_name = "examinations/create.html"
    model = Examination
    fields = "__all__"
    success_url = reverse_lazy("examination_list")


class ExaminationDeleteView(DoctorMixin, DeleteView):
    template_name = "examinations/confirm_delete.html"
    model = Examination
    success_url = reverse_lazy("examination_list")


class ExaminationDetailView(InternMixin, DetailView):
    template_name = "examinations/detail.html"
    model = Examination
