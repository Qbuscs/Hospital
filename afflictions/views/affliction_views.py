from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from users.mixins import DoctorMixin, InternMixin

from afflictions.models import Affliction


class AfflictionCreateView(DoctorMixin, CreateView):
    template_name = "afflictions/create.html"
    model = Affliction
    fields = ["name"]
    success_url = reverse_lazy("affliction_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["operation"] = "create"
        return context


class AfflictionUpdateView(DoctorMixin, UpdateView):
    template_name = "afflictions/create.html"
    model = Affliction
    fields = ["name"]
    success_url = reverse_lazy("affliction_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["operation"] = "edit"
        return context


class AfflictionListView(InternMixin, ListView):
    template_name = "afflictions/list.html"
    model = Affliction


class AfflictionDeleteView(DoctorMixin, DeleteView):
    template_name = "afflictions/confirm_delete.html"
    model = Affliction
    success_url = reverse_lazy("affliction_list")
