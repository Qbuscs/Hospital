from django.views.generic import ListView, CreateView, CreateView, DeleteView
from django.urls import reverse_lazy

from .models import Affliction, Sickness
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
    fields = ["afflictions", "name"]
    success_url = reverse_lazy("sickness_list")


class SicknessListView(InternMixin, ListView):
    model = Sickness


class SicknessDeleteView(DoctorMixin, DeleteView):
    model = Sickness
    success_url = reverse_lazy("sickness_list")