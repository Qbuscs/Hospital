from django.views.generic import ListView, CreateView, CreateView, DeleteView, DetailView
from django.urls import reverse_lazy

from .models import Affliction, Sickness, Medicine, Parasite
from users.mixins import InternMixin, DoctorMixin


class AfflictionCreateView(DoctorMixin, CreateView):
    model = Affliction
    fields = ["name"]
    success_url = reverse_lazy("afflictions_list")


class AfflictionListView(InternMixin, ListView):
    model = Affliction


class AfflictionDeleteView(DoctorMixin, DeleteView):
    model = Affliction
    success_url = reverse_lazy("afflictions_list")


class SicknessCreateView(DoctorMixin, CreateView):
    model = Sickness
    fields = ["name", "afflictions"]
    success_url = reverse_lazy("sickness_list")


class SicknessListView(InternMixin, ListView):
    model = Sickness


class SicknessDeleteView(DoctorMixin, DeleteView):
    model = Sickness
    success_url = reverse_lazy("sickness_list")


class SicknessDetailView(InternMixin, DetailView):
    model = Sickness


class MedicineCreateView(DoctorMixin, CreateView):
    model = Medicine
    fields = ["name"]
    success_url = reverse_lazy("medicine_list")


class MedicineListView(InternMixin, ListView):
    model = Medicine


class MedicineDeleteView(DoctorMixin, DeleteView):
    model = Medicine
    success_url = reverse_lazy("medicine_list")


class MedicineDetailView(InternMixin, DetailView):
    model = Medicine


class ParasiteCreateView(DoctorMixin, CreateView):
    model = Parasite
    fields = ["name", "afflictions"]
    success_url = reverse_lazy("parasite_list")


class ParasiteListView(InternMixin, ListView):
    model = Parasite


class ParasiteDeleteView(DoctorMixin, DeleteView):
    model = Parasite
    success_url = reverse_lazy("parasite_list")


class ParasiteDetailView(InternMixin, DetailView):
    model = Parasite
