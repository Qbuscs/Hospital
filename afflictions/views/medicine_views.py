from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from users.mixins import DoctorMixin, InternMixin

from afflictions.models import Medicine


class MedicineCreateView(DoctorMixin, CreateView):
    template_name = "medicine/create.html"
    model = Medicine
    fields = ["name"]
    success_url = reverse_lazy("medicine_list")


class MedicineUpdateView(DoctorMixin, UpdateView):
    template_name = "medicine/create.html"
    model = Medicine
    fields = ["name"]

    def get_success_url(self):
        return reverse_lazy("medicine_detail", kwargs={"pk": self.object.pk})


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