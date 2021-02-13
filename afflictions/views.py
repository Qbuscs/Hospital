from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView
from users.mixins import DoctorMixin, InternMixin

from .models import Affliction, Medicine, Parasite, Sickness, Fungus


class AfflictionCreateView(DoctorMixin, CreateView):
    template_name = "afflictions/create.html"
    model = Affliction
    fields = ["name"]
    success_url = reverse_lazy("affliction_list")


class AfflictionListView(InternMixin, ListView):
    template_name = "afflictions/list.html"
    model = Affliction


class AfflictionDeleteView(DoctorMixin, DeleteView):
    template_name = "afflictions/confirm_delete.html"
    model = Affliction
    success_url = reverse_lazy("affliction_list")


class SicknessCreateView(DoctorMixin, CreateView):
    template_name = "sicknesses/create.html"
    model = Sickness
    fields = ["name", "afflictions"]
    success_url = reverse_lazy("sickness_list")


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


class MedicineCreateView(DoctorMixin, CreateView):
    template_name = "medicine/create.html"
    model = Medicine
    fields = ["name"]
    success_url = reverse_lazy("medicine_list")


class MedicineListView(InternMixin, ListView):
    template_name = "medicine/list.html"
    model = Medicine


class MedicineDeleteView(DoctorMixin, DeleteView):
    template_name = "medicine/confirm_delete.html"
    model = Medicine
    success_url = reverse_lazy("medicine_list")


class MedicineDetailView(InternMixin, DetailView):
    template_name = "medicine/detail.html"
    model = Medicine


class ParasiteCreateView(DoctorMixin, CreateView):
    template_name = "parasites/create.html"
    model = Parasite
    fields = ["name", "afflictions"]
    success_url = reverse_lazy("parasite_list")


class ParasiteListView(InternMixin, ListView):
    template_name = "parasites/list.html"
    model = Parasite


class ParasiteDeleteView(DoctorMixin, DeleteView):
    template_name = "parasites/confirm_delete.html"
    model = Parasite
    success_url = reverse_lazy("parasite_list")


class ParasiteDetailView(InternMixin, DetailView):
    template_name = "parasites/detail.html"
    model = Parasite


class FungusCreateView(DoctorMixin, CreateView):
    template_name = "fungi/create.html"
    model = Fungus
    fields = "__all__"
    success_url = reverse_lazy("fungus_list")


class FungusListView(InternMixin, ListView):
    template_name = "fungi/list.html"
    model = Fungus


class FungusDeleteView(DoctorMixin, DeleteView):
    template_name = "fungi/confirm_delete.html"
    model = Fungus
    success_url = reverse_lazy("fungus_list")


class FungusDetailView(InternMixin, DetailView):
    template_name = "fungi/detail.html"
    model = Fungus
