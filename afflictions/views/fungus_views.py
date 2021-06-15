from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from users.mixins import DoctorMixin, InternMixin

from afflictions.models import Fungus
from hospital.mixins import OrderableMixin, SearchableMixin, CSVMixin


class FungusCreateView(DoctorMixin, CreateView):
    template_name = "fungi/create.html"
    model = Fungus
    fields = "__all__"
    success_url = reverse_lazy("fungus_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["operation"] = "create"
        return context


class FungusUpdateView(DoctorMixin, UpdateView):
    template_name = "fungi/create.html"
    model = Fungus
    fields = "__all__"

    def get_success_url(self):
        return reverse_lazy("fungus_detail", kwargs={"pk": self.object.id})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["operation"] = "edit"
        return context


class FungusListView(InternMixin, OrderableMixin, SearchableMixin, CSVMixin, ListView):
    template_name = "fungi/list.html"
    model = Fungus
    paginate_by = 10
    search_fields = [("name", "icontains")]


class FungusDeleteView(DoctorMixin, DeleteView):
    template_name = "fungi/confirm_delete.html"
    model = Fungus
    success_url = reverse_lazy("fungus_list")


class FungusDetailView(InternMixin, DetailView):
    template_name = "fungi/detail.html"
    model = Fungus
