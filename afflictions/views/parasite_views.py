from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from users.mixins import DoctorMixin, InternMixin

from afflictions.models import Parasite
from hospital.mixins import OrderableMixin, SearchableMixin


class ParasiteCreateView(DoctorMixin, CreateView):
    template_name = "parasites/create.html"
    model = Parasite
    fields = ["name", "afflictions"]
    success_url = reverse_lazy("parasite_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["operation"] = "create"
        return context


class ParasiteUpdateView(DoctorMixin, UpdateView):
    template_name = "parasites/create.html"
    model = Parasite
    fields = ["name", "afflictions"]
    success_url = reverse_lazy("parasite_list")

    def get_success_url(self):
        return reverse_lazy("parasite_detail", kwargs={"pk": self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["operation"] = "edit"
        return context


class ParasiteListView(InternMixin, OrderableMixin, SearchableMixin, ListView):
    template_name = "parasites/list.html"
    model = Parasite
    search_fields = ["name"]


class ParasiteDeleteView(DoctorMixin, DeleteView):
    template_name = "parasites/confirm_delete.html"
    model = Parasite
    success_url = reverse_lazy("parasite_list")


class ParasiteDetailView(InternMixin, DetailView):
    template_name = "parasites/detail.html"
    model = Parasite
