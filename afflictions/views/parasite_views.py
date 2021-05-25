from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from users.mixins import DoctorMixin, InternMixin

from afflictions.models import Parasite
from afflictions.utils import get_parasite_species_list_safe
from hospital.mixins import OrderableMixin, SearchableMixin, CSVMixin


class ParasiteCreateView(DoctorMixin, CreateView):
    template_name = "parasites/create.html"
    model = Parasite
    fields = ["species", "subtype", "afflictions"]
    success_url = reverse_lazy("parasite_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["operation"] = "create"
        context["parasite_species"] = get_parasite_species_list_safe()
        print(context["parasite_species"])
        return context


class ParasiteUpdateView(DoctorMixin, UpdateView):
    template_name = "parasites/create.html"
    model = Parasite
    fields = ["species", "subtype", "afflictions"]
    success_url = reverse_lazy("parasite_list")

    def get_success_url(self):
        return reverse_lazy("parasite_detail", kwargs={"pk": self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["operation"] = "edit"
        context["parasite_species"] = get_parasite_species_list_safe()
        print(context["parasite_species"])
        return context


class ParasiteListView(InternMixin, OrderableMixin, SearchableMixin, CSVMixin, ListView):
    template_name = "parasites/list.html"
    model = Parasite
    paginate_by = 10
    search_fields = [("species", "icontains"), ("subtype", "icontains")]


class ParasiteDeleteView(DoctorMixin, DeleteView):
    template_name = "parasites/confirm_delete.html"
    model = Parasite
    success_url = reverse_lazy("parasite_list")


class ParasiteDetailView(InternMixin, DetailView):
    template_name = "parasites/detail.html"
    model = Parasite
