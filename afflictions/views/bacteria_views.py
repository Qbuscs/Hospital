from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from users.mixins import DoctorMixin, InternMixin

from afflictions.models import Bacteria
from hospital.mixins import OrderableMixin, SearchableMixin, CSVMixin


class BacteriaCreateView(DoctorMixin, CreateView):
    template_name = "bacteria/create.html"
    model = Bacteria
    fields = "__all__"
    success_url = reverse_lazy("bacteria_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["operation"] = "create"
        return context


class BacteriaUpdateView(DoctorMixin, UpdateView):
    template_name = "bacteria/create.html"
    model = Bacteria
    fields = "__all__"

    def get_success_url(self):
        return reverse_lazy("bacteria_detail", kwargs={"pk": self.object.id})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["operation"] = "edit"
        return context


class BacteriaListView(InternMixin, OrderableMixin, SearchableMixin, CSVMixin, ListView):
    template_name = "bacteria/list.html"
    model = Bacteria
    paginate_by = 10
    search_fields = [("name", "icontains")]


class BacteriaDeleteView(DoctorMixin, DeleteView):
    template_name = "bacteria/confirm_delete.html"
    model = Bacteria
    success_url = reverse_lazy("bacteria_list")


class BacteriaDetailView(InternMixin, DetailView):
    template_name = "bacteria/detail.html"
    model = Bacteria
