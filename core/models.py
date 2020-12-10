from django.db import models
from django.utils.translation import gettext_lazy as _

from afflictions.models import Affliction, Sickness, SicknessExamination, Fungus, FungusExamination, Parasite
from animals.models import AnimalExamination, Animal


class Patient(models.Model):
    EDUCATION_NONE = 0
    EDUCATION_PRIMARY = 1
    EDUCATION_SECONDARY = 2
    EDUCATION_HIGHER = 3

    EDUCATION_CHOICES = (
        (EDUCATION_NONE, _("brak")),
        (EDUCATION_PRIMARY, _("podstawowe")),
        (EDUCATION_SECONDARY, _("średnie")),
        (EDUCATION_HIGHER, _("wyższe")),
    )

    GENDER_MALE = 1
    GENDER_FEMALE = 2
    GENDER_OTHER = 3

    GENDER_CHOICES = (
        (GENDER_MALE, _("mężczyzna")),
        (GENDER_FEMALE, _("kobieta")),
        (GENDER_OTHER, _("inna")),
    )

    first_name = models.CharField(_("imię"), null=False, blank=False, max_length=200)
    last_name = models.CharField(_("nazwisko"), null=False, blank=False, max_length=200)
    education = models.PositiveSmallIntegerField(_("wykształcenie"), choices=EDUCATION_CHOICES, null=False)
    gender = models.PositiveSmallIntegerField(_("płeć"), choices=GENDER_CHOICES, null=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = _("pacjent")
        verbose_name_plural = _("pacjenci")


class Examination(models.Model):
    patient = models.ForeignKey(Patient, verbose_name=_("pacjent"), on_delete=models.PROTECT, null=False, blank=False)
    date = models.DateField(_("data"), null=False)
    animals = models.ManyToManyField(Animal, through=AnimalExamination, related_name="examinations")
    afflictions = models.ManyToManyField(Affliction, verbose_name=_("objawy"), related_name="examinations", blank=True)
    sicknesses = models.ManyToManyField(Sickness, related_name="examinations", through=SicknessExamination)
    fungi = models.ManyToManyField(Fungus, related_name="examinations", through=FungusExamination)
    parasites = models.ManyToManyField(Parasite, related_name="examinations", verbose_name=_("pasożyty"), blank=True)

    # histopathological examinations
    collagen_layer_thickening = models.BooleanField(
        _("pogrubienie warstwy kolagenu u podstawy komórek nabłonka"),
        null=True,
        blank=True
    )
    increased_intraepithelial_lymphocytes = models.BooleanField(
        _("zwiększona liczba limfocytów śródnabłonkowych"),
        null=True,
        blank=True
    )
    lymphocytes_infiltration = models.BooleanField(_("naciek z limfocytów"), null=True, blank=True)
    plasmocytes_infiltration = models.BooleanField(_("naciek z plazmocytów"), null=True, blank=True)
    eosinophils_infiltration = models.BooleanField(_("naciek z eozynofili"), null=True, blank=True)
    mast_cells_infiltration = models.BooleanField(_("naciek z komórek tucznych"), null=True, blank=True)
    neutrocytes_infiltration = models.BooleanField(_("naciek z neutrocytów"), null=True, blank=True)

    # TODO: morfologia


    def __str__(self):
        return f"{self.patient} - {self.date}"

    class Meta:
        verbose_name = _("Badanie"),
        verbose_name_plural = _("Badania")

