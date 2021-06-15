from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from users.mixins import DoctorMixin, InternMixin

from afflictions.models import Virus
from hospital.mixins import OrderableMixin, SearchableMixin, CSVMixin


class VirusCreateView(DoctorMixin, CreateView):
    template_name = "viruses/create.html"
    model = Virus
    fields = "__all__"
    success_url = reverse_lazy("virus_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["operation"] = "create"
        return context


class VirusUpdateView(DoctorMixin, UpdateView):
    template_name = "viruses/create.html"
    model = Virus
    fields = "__all__"

    def get_success_url(self):
        return reverse_lazy("virus_detail", kwargs={"pk": self.object.id})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["operation"] = "edit"
        return context


class VirusListView(InternMixin, OrderableMixin, SearchableMixin, CSVMixin, ListView):
    template_name = "viruses/list.html"
    model = Virus
    paginate_by = 10
    search_fields = [("name", "icontains")]


class VirusDeleteView(DoctorMixin, DeleteView):
    template_name = "viruses/confirm_delete.html"
    model = Virus
    success_url = reverse_lazy("virus_list")


class VirusDetailView(InternMixin, DetailView):
    template_name = "viruses/detail.html"
    model = Virus
