from django.db import transaction
from django.views.generic import ListView, CreateView, DeleteView, DetailView
from django.urls import reverse_lazy

from .models import Patient, Examination
from .forms import ExaminationForm
from afflictions.forms import SicknessExaminationFormSet, MedicineExaminationFormSet, FungusExaminationFormSet
from animals.forms import AnimalExaminationFormSet
from travels.forms import TravelFormSet
from users.mixins import InternMixin, DoctorMixin


class PatientListView(InternMixin, ListView):
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


class ExaminationListView(InternMixin, ListView):
    template_name = "examinations/list.html"
    model = Examination


class ExaminationCreateView(DoctorMixin, CreateView):
    template_name = "examinations/create.html"
    model = Examination
    success_url = reverse_lazy("examination_list")
    form_class = ExaminationForm

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
        return context
    
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


class ExaminationDeleteView(DoctorMixin, DeleteView):
    template_name = "examinations/confirm_delete.html"
    model = Examination
    success_url = reverse_lazy("examination_list")


class ExaminationDetailView(InternMixin, DetailView):
    template_name = "examinations/detail.html"
    model = Examination
