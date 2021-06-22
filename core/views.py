import csv

from afflictions import models as afflictions_models
from afflictions.forms import (BacteriaExaminationFormSet,
                               FungusExaminationFormSet,
                               MedicineExaminationFormSet,
                               SicknessExaminationFormSet)
from animals.forms import AnimalExaminationFormSet
from animals.models import AnimalExamination
from django.contrib import messages
from django.db import transaction
from django.forms import (ChoiceField, DateField, IntegerField,
                          ModelChoiceField, ModelMultipleChoiceField,
                          TextInput, ValidationError)
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.translation import gettext
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from hospital.mixins import CSVMixin, OrderableMixin, SearchableMixin
from hospital.utils import str_to_int_or_none
from morphologies.forms import MorphologyExaminationFormSet
from travels.forms import TravelFormSet
from travels.models import Travel
from travels.utils import get_coords
from users.mixins import DoctorMixin, InternMixin

from .forms import ExaminationForm
from .models import Examination, Patient
from .utils import (filter_examinations_fungus_resistance,
                    filter_examinations_travel_time,
                    get_travels_from_examinations)


class PatientListView(InternMixin, OrderableMixin, SearchableMixin, CSVMixin, ListView):
    template_name = "patients/list.html"
    model = Patient
    paginate_by = 10
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
    paginate_by = 10
    search_fields = []
    search_fields_omitted = (
        "travel_time_country", "travel_time_days_min", "travel_time_days_max", "fungus_resistance_fungus",
        "fungus_resistance_medicine", "fungus_resistance_resistance"
    )

    def get_extra_search_fields(self):
        date_from_field = DateField(label=gettext("Data od"), widget=TextInput(attrs={"autocomplete": "off"}))
        date_to_field = DateField(label=gettext("Data do"), widget=TextInput(attrs={"autocomplete": "off"}))
        first_name_field = Patient._meta.get_field("first_name").formfield()
        last_name_field = Patient._meta.get_field("last_name").formfield()
        gender_field = Patient._meta.get_field("gender").formfield()
        education_field = Patient._meta.get_field("education").formfield()
        age_min_field = Patient._meta.get_field("age").formfield()
        age_max_field = Patient._meta.get_field("age").formfield()
        country_field = Travel._meta.get_field("country").formfield()
        visit_field = Travel._meta.get_field("visit").formfield()
        specificity_field = Travel._meta.get_field("specificity").formfield()

        first_name_field.label = gettext("Imię pacjenta")
        last_name_field.label = gettext("Nazwisko pacjenta")
        gender_field.label = gettext("Płeć pacjenta")
        age_min_field.label = gettext("Wiek pacjenta (minimum)")
        age_max_field.label = gettext("Wiek pacjenta (maksimum)")
        education_field.label = gettext("Wykształcenie pacjenta")
        country_field.label = gettext("Kraj podróży")
        visit_field.label = gettext("Rodzaj wizyty")
        specificity_field.label = gettext("Stosowana profilaktyka")

        afflictions_qs = afflictions_models.Affliction.objects.all()
        parasites_qs = afflictions_models.Parasite.objects.all()
        sickness_qs = afflictions_models.Sickness.objects.all()
        fungus_qs = afflictions_models.Fungus.objects.all()
        bacteria_qs = afflictions_models.Bacteria.objects.all()
        virus_qs = afflictions_models.Virus.objects.all()
        medicine_qs = afflictions_models.Medicine.objects.all()
        
        afflictions_field_or = ModelMultipleChoiceField(queryset=afflictions_qs, label=gettext("Objawy (dowolne)"))
        afflictions_field_and = ModelMultipleChoiceField(queryset=afflictions_qs, label=gettext("Objawy (wszystkie)"))
        parasites_field_or = ModelMultipleChoiceField(queryset=parasites_qs, label=gettext("Pasożyty (dowolne)"))
        parasites_field_and = ModelMultipleChoiceField(queryset=parasites_qs, label=gettext("Pasożyty (wszystkie)"))
        sickness_field_or = ModelMultipleChoiceField(queryset=sickness_qs, label=gettext("Choroby (dowolne)"))
        sickness_field_and = ModelMultipleChoiceField(queryset=sickness_qs, label=gettext("Choroby (wszystkie)"))
        fungus_field_or = ModelMultipleChoiceField(queryset=fungus_qs, label=gettext("Grzyby (dowolne)"))
        fungus_field_and = ModelMultipleChoiceField(queryset=fungus_qs, label=gettext("Grzyby (wszystkie)"))
        bacteria_field_or = ModelMultipleChoiceField(queryset=bacteria_qs, label=gettext("Bakterie (dowolne)"))
        bacteria_field_and = ModelMultipleChoiceField(queryset=bacteria_qs, label=gettext("Bakterie (wszystkie)"))
        virus_field_or = ModelMultipleChoiceField(queryset=virus_qs, label=gettext("Wirusy (dowolne)"))
        virus_field_and = ModelMultipleChoiceField(queryset=virus_qs, label=gettext("Wirusy (wszystkie)"))

        # CUSTOM FIELDS
        travel_time_country_field = Travel._meta.get_field("country").formfield()
        travel_time_country_field.label = gettext("Czas podróży (kraj)")
        travel_time_days_min_field = IntegerField(min_value=1, label=gettext("Czas podrózy (minimum dni)"))
        travel_time_days_max_field = IntegerField(min_value=1, label=gettext("Czas podrózy (maksimum dni)"))
        fungus_resistance_fungus_field = ModelChoiceField(queryset=fungus_qs, label=gettext("Oporność (grzyb)"))
        fungus_resistance_medicine_field = ModelChoiceField(queryset=medicine_qs, label=gettext("Oporność (lek)"))
        fungus_resistance_resistance_field = ChoiceField(
            choices=(
                ("", "---------"),
                (0, gettext("oporny")),
                (1, gettext("średnio wrażliwy")),
                (2, gettext("wrażliwy"))
            ),
            label=gettext("Oporność (stopień)")
        )
        return {
            "patient__first_name": (first_name_field, "icontains"),
            "patient__last_name": (last_name_field, "icontains"),
            "patient__gender": (gender_field, "icontains"),
            "patient__age__gte": (age_min_field, None),
            "patient__age__lte": (age_min_field, None),
            "patient__education": (education_field, "icontains"),
            "afflictions__OR": (afflictions_field_or, "in"),
            "afflictions__AND": (afflictions_field_and, "in"),
            "parasites__OR": (parasites_field_or, "in"),
            "parasites__AND": (parasites_field_and, "in"),
            "sicknesses__sickness__OR": (sickness_field_or, "in"),
            "sicknesses__sickness__AND": (sickness_field_and, "in"),
            "fungi__fungus__OR": (fungus_field_or, "in"),
            "fungi__fungus__AND": (fungus_field_and, "in"),
            "bacteria__bacteria__OR": (bacteria_field_or, "in"),
            "bacteria__bacteria__AND": (bacteria_field_and, "in"),
            "viruses__OR": (virus_field_or, "in"),
            "viruses__AND": (virus_field_and, "in"),
            "date__gte": (date_from_field, None),
            "date__lte": (date_to_field, None),
            "travels__country": (country_field, "icontains"),
            "travels__visit": (visit_field, "icontains"),
            "travels__specificity": (specificity_field, "icontains"),
            "travel_time_country": (travel_time_country_field, None),
            "travel_time_days_min": (travel_time_days_min_field, None),
            "travel_time_days_max": (travel_time_days_max_field, None),
            "fungus_resistance_fungus": (fungus_resistance_fungus_field, None),
            "fungus_resistance_medicine": (fungus_resistance_medicine_field, None),
            "fungus_resistance_resistance": (fungus_resistance_resistance_field, None),
        }

    def custom_filters(self, queryset):
        travel_time_country = self.request.GET.get("travel_time_country")
        travel_time_days_min = str_to_int_or_none(self.request.GET.get("travel_time_days_min"))
        travel_time_days_max = str_to_int_or_none(self.request.GET.get("travel_time_days_max"))
        if travel_time_country and (travel_time_days_min or travel_time_days_max):
            queryset = filter_examinations_travel_time(
                queryset, travel_time_country, travel_time_days_min, travel_time_days_max
            )
        fungus_resistance_fungus = str_to_int_or_none(self.request.GET.get("fungus_resistance_fungus"))
        fungus_resistance_medicine = str_to_int_or_none(self.request.GET.get("fungus_resistance_medicine"))
        fungus_resistance_resistance = str_to_int_or_none(self.request.GET.get("fungus_resistance_resistance"))
        if fungus_resistance_fungus and fungus_resistance_medicine:
            queryset = filter_examinations_fungus_resistance(
                queryset, fungus_resistance_fungus, fungus_resistance_medicine, fungus_resistance_resistance
            )
        return queryset

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.select_related("patient")
        queryset = queryset.prefetch_related(
            "afflictions", "parasites", "viruses", "sicknesses", "sicknesses__sickness",
            "fungi", "fungi__fungus", "medicines", "medicines__medicine",
            "travels", "morphologies", "morphologies__morphology", "animals",
            "animals__animal", "bacteria__bacteria"
        )
        queryset = self.custom_filters(queryset)
        return queryset

    def build_animals_row(self, examination):
        animals = examination.animals.all()
        animals_row = []
        for animal in animals:
            animals_row.append({
                "name": animal.animal.name,
                "contact": AnimalExamination.CONTACT_CHOICES[animal.contact][1],
                "saliva": animal.saliva,
                "excrement": animal.excrement
            })
        return animals_row

    def build_travels_row(self, examination):
        travels = examination.travels.all()
        travels_row = []
        for travel in travels:
            travels_row.append({
                "country": travel.country.name,
                "date_start": travel.date_start.strftime("%d/%m/%Y"),
                "date_end": travel.date_end.strftime("%d/%m/%Y")
            })
        return travels_row

    def build_morphologies_row(self, examination):
        morphologies = examination.morphologies.all()
        morphologies_row = []
        for morphology in morphologies:
            morphologies_row.append({
                "morphology": morphology.morphology.name,
                "value": morphology.value,
                "unit": morphology.morphology.unit,
                "norm": morphology.norm_str()
            })
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
            gettext("bakterie"),
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
                list(obj.afflictions.values("name")),
                list(obj.sicknesses.values("sickness__name")),
                list(obj.parasites.values("species", "subtype")),
                list(obj.fungi.values("fungus__name", "amount", "high_resistance", "mid_resistance", "low_resistance")),
                list(obj.bacteria.values("bacteria__name", "high_resistance", "mid_resistance", "low_resistance")),
                list(obj.medicines.values("medicine__name", "amount", "unit")),
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
        examinations = super().get_queryset().prefetch_related("travels")
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
        bacteria = context["bacteria"]
        try:
            with transaction.atomic():
                self.object = form.save()
                for related in [sicknesses, medicines, fungi, animals, travels, morphologies, bacteria]:
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
            context["bacteria"] = BacteriaExaminationFormSet(self.request.POST)
        else:
            context["sicknesses"] = SicknessExaminationFormSet()
            context["medicines"] = MedicineExaminationFormSet()
            context["fungi"] = FungusExaminationFormSet()
            context["animals"] = AnimalExaminationFormSet()
            context["travels"] = TravelFormSet()
            context["morphologies"] = MorphologyExaminationFormSet()
            context["bacteria"] = BacteriaExaminationFormSet()
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
            context["bacteria"] = BacteriaExaminationFormSet(self.request.POST, instance=self.object)
        else:
            context["sicknesses"] = SicknessExaminationFormSet(instance=self.object)
            context["medicines"] = MedicineExaminationFormSet(instance=self.object)
            context["fungi"] = FungusExaminationFormSet(instance=self.object)
            context["animals"] = AnimalExaminationFormSet(instance=self.object)
            context["travels"] = TravelFormSet(instance=self.object)
            context["morphologies"] = MorphologyExaminationFormSet(instance=self.object)
            context["bacteria"] = BacteriaExaminationFormSet(instance=self.object)
        context["operation"] = "edit"
        return context


class ExaminationDeleteView(DoctorMixin, DeleteView):
    template_name = "examinations/confirm_delete.html"
    model = Examination
    success_url = reverse_lazy("examination_list")


class ExaminationDetailView(InternMixin, DetailView):
    template_name = "examinations/detail.html"
    model = Examination
