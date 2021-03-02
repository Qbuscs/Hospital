from afflictions.forms import (FungusExaminationFormSet,
                               MedicineExaminationFormSet,
                               SicknessExaminationFormSet)
from animals.forms import AnimalExaminationFormSet
from django.db import transaction
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from hospital.mixins import OrderableMixin
from travels.forms import TravelFormSet
from users.mixins import DoctorMixin, InternMixin

from .forms import ExaminationForm
from .models import Examination, Patient


class PatientListView(InternMixin, OrderableMixin, ListView):
    template_name = "patients/list.html"
    model = Patient


class PatientDeleteView(DoctorMixin, DeleteView):
    template_name = "patients/confirm_delete.html"
    model = Patient
    success_url = reverse_lazy("patient_list")


class PatientCreateView(DoctorMixin, CreateView):
    template_name = "patients/create.html"
    model = Patient
    fields = "__all__"
    success_url = reverse_lazy("patient_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["operation"] = "create"
        return context


class PatientDetailView(InternMixin, DetailView):
    template_name = "patients/detail.html"
    model = Patient


class PatientUpdateView(DoctorMixin, UpdateView):
    template_name = "patients/create.html"
    model = Patient
    fields = "__all__"
    success_url = reverse_lazy("patient_list")

    def get_success_url(self):
        return reverse_lazy("patient_detail", kwargs={"pk": self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["operation"] = "edit"
        return context


class ExaminationListView(InternMixin, OrderableMixin, ListView):
    template_name = "examinations/list.html"
    model = Examination


class ExaminationFormView:
    template_name = "examinations/create.html"
    model = Examination
    success_url = reverse_lazy("examination_list")
    form_class = ExaminationForm

    def form_valid(self, form):
        context = self.get_context_data()
        sicknesses = context["sicknesses"]
        medicines = context["medicines"]
        fungi = context["fungi"]
        animals = context["animals"]
        travels = context["travels"]
        with transaction.atomic():
            self.object = form.save()
            for related in [sicknesses, medicines, fungi, animals, travels]:
                if related.is_valid():
                    related.instance = self.object
                    related.save()
        return super().form_valid(form)


class ExaminationCreateView(DoctorMixin, ExaminationFormView, CreateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context["sicknesses"] = SicknessExaminationFormSet(self.request.POST)
            context["medicines"] = MedicineExaminationFormSet(self.request.POST)
            context["fungi"] = FungusExaminationFormSet(self.request.POST)
            context["animals"] = AnimalExaminationFormSet(self.request.POST)
            context["travels"] = TravelFormSet(self.request.POST)
        else:
            context["sicknesses"] = SicknessExaminationFormSet()
            context["medicines"] = MedicineExaminationFormSet()
            context["fungi"] = FungusExaminationFormSet()
            context["animals"] = AnimalExaminationFormSet()
            context["travels"] = TravelFormSet()
        context["operation"] = "create"
        return context


class ExaminationUpdateView(DoctorMixin, ExaminationFormView, UpdateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context["sicknesses"] = SicknessExaminationFormSet(self.request.POST, instance=self.object)
            context["medicines"] = MedicineExaminationFormSet(self.request.POST, instance=self.object)
            context["fungi"] = FungusExaminationFormSet(self.request.POST, instance=self.object)
            context["animals"] = AnimalExaminationFormSet(self.request.POST, instance=self.object)
            context["travels"] = TravelFormSet(self.request.POST, instance=self.object)
        else:
            context["sicknesses"] = SicknessExaminationFormSet(instance=self.object)
            context["medicines"] = MedicineExaminationFormSet(instance=self.object)
            context["fungi"] = FungusExaminationFormSet(instance=self.object)
            context["animals"] = AnimalExaminationFormSet(instance=self.object)
            context["travels"] = TravelFormSet(instance=self.object)
        context["operation"] = "edit"
        return context


class ExaminationDeleteView(DoctorMixin, DeleteView):
    template_name = "examinations/confirm_delete.html"
    model = Examination
    success_url = reverse_lazy("examination_list")


class ExaminationDetailView(InternMixin, DetailView):
    template_name = "examinations/detail.html"
    model = Examination
