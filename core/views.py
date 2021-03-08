from afflictions.forms import (FungusExaminationFormSet,
                               MedicineExaminationFormSet,
                               SicknessExaminationFormSet)
from animals.forms import AnimalExaminationFormSet
from django.contrib import messages
from django.db import transaction
from django.forms import ValidationError
from django.urls import reverse_lazy
from django.utils.translation import gettext
from django.shortcuts import render
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from hospital.mixins import OrderableMixin, SearchableMixin
from travels.forms import TravelFormSet
from users.mixins import DoctorMixin, InternMixin
from morphologies.forms import MorphologyExaminationFormSet

from .forms import ExaminationForm
from .models import Examination, Patient


class PatientListView(InternMixin, OrderableMixin, SearchableMixin, ListView):
    template_name = "patients/list.html"
    model = Patient
    search_fields = ["first_name", "last_name", "gender", "age", "education"]


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


class ExaminationListView(InternMixin, OrderableMixin, SearchableMixin, ListView):
    template_name = "examinations/list.html"
    model = Examination
    search_fields = ["date"]

    def get_extra_search_fields(self):
        first_name_field = Patient._meta.get_field("first_name").formfield()
        last_name_field = Patient._meta.get_field("last_name").formfield()
        first_name_field.label = gettext("Imię pacjenta")
        last_name_field.label = gettext("Nazwisko pacjenta")
        return {"patient__first_name": first_name_field, "patient__last_name": last_name_field}

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.select_related("patient")


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
        morphologies = context["morphologies"]
        try:
            with transaction.atomic():
                self.object = form.save()
                for related in [sicknesses, medicines, fungi, animals, travels, morphologies]:
                    if related.is_valid():
                        related.instance = self.object
                        related.save()
                    else:
                        raise ValidationError(related.errors)    
        except ValidationError:
            messages.error(self.request, gettext("W formularzu znajdują się błędy. Zjedź niżej po więcej szczegółów."))
            return render(self.request, self.template_name, context)
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
            context["morphologies"] = MorphologyExaminationFormSet(self.request.POST)
        else:
            context["sicknesses"] = SicknessExaminationFormSet()
            context["medicines"] = MedicineExaminationFormSet()
            context["fungi"] = FungusExaminationFormSet()
            context["animals"] = AnimalExaminationFormSet()
            context["travels"] = TravelFormSet()
            context["morphologies"] = MorphologyExaminationFormSet()
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
            context["morphologies"] = MorphologyExaminationFormSet(self.request.POST, instance=self.object)
        else:
            context["sicknesses"] = SicknessExaminationFormSet(instance=self.object)
            context["medicines"] = MedicineExaminationFormSet(instance=self.object)
            context["fungi"] = FungusExaminationFormSet(instance=self.object)
            context["animals"] = AnimalExaminationFormSet(instance=self.object)
            context["travels"] = TravelFormSet(instance=self.object)
            context["morphologies"] = MorphologyExaminationFormSet(instance=self.object)
        context["operation"] = "edit"
        return context


class ExaminationDeleteView(DoctorMixin, DeleteView):
    template_name = "examinations/confirm_delete.html"
    model = Examination
    success_url = reverse_lazy("examination_list")


class ExaminationDetailView(InternMixin, DetailView):
    template_name = "examinations/detail.html"
    model = Examination
