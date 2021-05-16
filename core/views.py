import csv

from afflictions.forms import (FungusExaminationFormSet,
                               MedicineExaminationFormSet,
                               SicknessExaminationFormSet)
from afflictions import models as afflictions_models
from animals.forms import AnimalExaminationFormSet
from animals.models import AnimalExamination
from django.contrib import messages
from django.db import transaction
from django.forms import ValidationError, DateField, ModelMultipleChoiceField
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.utils.translation import gettext
from django.shortcuts import render
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from hospital.mixins import OrderableMixin, SearchableMixin, CSVMixin
from travels.forms import TravelFormSet
from travels.models import Travel
from travels.utils import get_coords
from users.mixins import DoctorMixin, InternMixin
from morphologies.forms import MorphologyExaminationFormSet

from .forms import ExaminationForm
from .models import Examination, Patient
from .utils import get_travels_from_examinations


class PatientListView(InternMixin, OrderableMixin, SearchableMixin, CSVMixin, ListView):
    template_name = "patients/list.html"
    model = Patient
    search_fields = [
        ("first_name", "icontains"),
        ("last_name", "icontains"),
        ("gender", "icontains"),
        ("age", "icontains"),
        ("education", "icontains")
    ]

    def get_csv_mapping(self):
        return {
            "education": lambda x: Patient.EDUCATION_CHOICES[x][1],
            "gender": lambda x: Patient.GENDER_CHOICES[x][1]
        }


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
    search_fields = [
        ("afflictions", "in"),
        ("parasites", "in"),
    ]

    def get_extra_search_fields(self):
        date_from_field = DateField(label=gettext("Data od"))
        date_to_field = DateField(label=gettext("Data do"))
        first_name_field = Patient._meta.get_field("first_name").formfield()
        last_name_field = Patient._meta.get_field("last_name").formfield()
        sickness_field = ModelMultipleChoiceField(
            queryset=afflictions_models.Sickness.objects.all(), label=gettext("Choroby")
        )
        fungus_field = ModelMultipleChoiceField(
            queryset=afflictions_models.Fungus.objects.all(), label=gettext("Grzyby")
        )
        country_field = Travel._meta.get_field("country").formfield()

        first_name_field.label = gettext("Imię pacjenta")
        last_name_field.label = gettext("Nazwisko pacjenta")
        country_field.label = gettext("Kraj podróży")
        return {
            "sicknesses__sickness": (sickness_field, "in"),
            "fungi__fungus": (fungus_field, "in"),
            "date__gte": (date_from_field, None),
            "date__lte": (date_to_field, None),
            "patient__first_name": (first_name_field, "icontains"),
            "patient__last_name": (last_name_field, "icontains"),
            "travels__country": (country_field, "icontains"),
        }

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.select_related("patient")
        queryset = queryset.prefetch_related(
            "afflictions", "parasites", "sicknesses", "sicknesses__sickness",
            "fungi", "fungi__fungus", "medicines", "medicines__medicine",
            "travels", "morphologies", "morphologies__morphology", "animals",
            "animals__animal"
        )
        return queryset

    def build_animals_row(self, examination):
        animals = examination.animals.all()
        animals_row = []
        for animal in animals:
            animals_row.append((
                animal.animal.name,
                AnimalExamination.CONTACT_CHOICES[animal.contact][1],
                animal.saliva,
                animal.excrement
            ))
        return animals_row

    def build_travels_row(self, examination):
        travels = examination.travels.all()
        travels_row = []
        for travel in travels:
            travels_row.append((
                travel.country.name,
                travel.date_start.strftime("%d/%m/%Y"),
                travel.date_end.strftime("%d/%m/%Y")
            ))
        return travels_row

    def build_morphologies_row(self, examination):
        morphologies = examination.morphologies.all()
        morphologies_row = []
        for morphology in morphologies:
            morphologies_row.append((
                morphology.morphology.name,
                morphology.value,
                morphology.morphology.unit,
                morphology.norm_str()
            ))
        return morphologies_row

    def get_csv(self):
        examinations = self.get_queryset()
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="examinations_export.csv"'
        writer = csv.writer(response, delimiter=";")
        writer.writerow([
            "ID",
            gettext("data"),
            gettext("imię pacjenta"),
            gettext("nazwisko pacjenta"),
            gettext("objawy"),
            gettext("choroby"),
            gettext("pasożyty (gatunek, subtyp)"),
            gettext("grzyby (gatunek, ilość)"),
            gettext("leki"),
            gettext("zwierzęta (gatunek, rodzaj kontaktu, kontakt ze śliną, kontakt z odchodami)"),
            gettext("podróże (kraj, start, powrót)"),
            gettext("badania morfologiczne (badanie, wynik, jednostka, norma)"),
            gettext("naciek z limfocytów"),
            gettext("naciek z plazmocytów"),
            gettext("naciek z eozynofili"),
            gettext("naciek z komórek tucznych"),
            gettext("naciek z neutrocytów"),
        ])
        for obj in examinations:
            writer.writerow([
                obj.id,
                obj.date,
                obj.patient.first_name,
                obj.patient.last_name,
                list(obj.afflictions.values_list("name")),
                list(obj.sicknesses.values_list("sickness__name")),
                list(obj.parasites.values_list("species", "subtype")),
                list(obj.fungi.values_list("fungus__name", "amount")),
                list(obj.medicines.values_list("medicine__name", "amount", "unit")),
                self.build_animals_row(obj),
                self.build_travels_row(obj),
                self.build_morphologies_row(obj),
                obj.lymphocytes_infiltration,
                obj.plasmocytes_infiltration,
                obj.eosinophils_infiltration,
                obj.mast_cells_infiltration,
                obj.neutrocytes_infiltration
            ])

        return response

    def get(self, request, *args, **kwargs):
        if "csv" in request.GET:
            return self.get_csv()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        examinations = super().get_queryset()
        travels = get_travels_from_examinations(examinations)
        context["coords"] = get_coords(travels)
        return context


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
