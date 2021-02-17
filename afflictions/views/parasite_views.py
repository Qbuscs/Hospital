from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from users.mixins import DoctorMixin, InternMixin

from afflictions.models import Parasite


class ParasiteCreateView(DoctorMixin, CreateView):
    template_name = "parasites/create.html"
    model = Parasite
    fields = ["name", "afflictions"]
    success_url = reverse_lazy("parasite_list")


class ParasiteUpdateView(DoctorMixin, UpdateView):
    template_name = "parasites/create.html"
    model = Parasite
    fields = ["name", "afflictions"]
    success_url = reverse_lazy("parasite_list")

    def get_success_url(self):
        return reverse_lazy("parasite_detail", kwargs={"pk": self.object.pk})


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
