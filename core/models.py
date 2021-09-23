from django.db import models
from django.utils.translation import gettext_lazy as _

from afflictions.models import (
    Affliction,
    Parasite,
    Virus,
    Vaccine
)


# class Patient(models.Model):
#     EDUCATION_NONE = 0
#     EDUCATION_PRIMARY = 1
#     EDUCATION_SECONDARY = 2
#     EDUCATION_HIGHER = 3

#     EDUCATION_CHOICES = (
#         (EDUCATION_NONE, _("brak")),
#         (EDUCATION_PRIMARY, _("podstawowe")),
#         (EDUCATION_SECONDARY, _("średnie")),
#         (EDUCATION_HIGHER, _("wyższe")),
#     )

#     GENDER_MALE = 0
#     GENDER_FEMALE = 1
#     GENDER_OTHER = 2

#     GENDER_CHOICES = (
#         (GENDER_MALE, _("mężczyzna")),
#         (GENDER_FEMALE, _("kobieta")),
#         (GENDER_OTHER, _("inna")),
#     )

#     first_name = models.CharField(_("imię"), null=False, blank=False, max_length=200)
#     last_name = models.CharField(_("nazwisko"), null=False, blank=False, max_length=200)
#     age = models.PositiveSmallIntegerField(_("wiek"), null=False, blank=False)
#     education = models.PositiveSmallIntegerField(_("wykształcenie"), choices=EDUCATION_CHOICES, null=False)
#     gender = models.PositiveSmallIntegerField(_("płeć"), choices=GENDER_CHOICES, null=False)

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"

#     class Meta:
#         verbose_name = _("pacjent")
#         verbose_name_plural = _("pacjenci")


class Examination(models.Model):
    HISTO_NONE = 0
    HISTO_WEAK = 1
    HISTO_MID = 2
    HISTO_HIGH = 3

    HISTO_CHOICES = (
        (HISTO_NONE, _("brak")),
        (HISTO_WEAK, _("mało")),
        (HISTO_MID, _("umiarkowany")),
        (HISTO_HIGH, _("intensywnie")),
    )

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

    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_OTHER = 2

    GENDER_CHOICES = (
        (GENDER_MALE, _("mężczyzna")),
        (GENDER_FEMALE, _("kobieta")),
        (GENDER_OTHER, _("inna")),
    )

    patient_age = models.PositiveSmallIntegerField(_("wiek pacjenta"), null=False, blank=False)
    patient_education = models.PositiveSmallIntegerField(_("wykształcenie pacjenta"), choices=EDUCATION_CHOICES, null=False)
    patient_gender = models.PositiveSmallIntegerField(_("płeć pacjenta"), choices=GENDER_CHOICES, null=False)
    date = models.DateField(_("data"), null=False)
    afflictions = models.ManyToManyField(Affliction, related_name="examinations", verbose_name=_("objawy"), blank=True)
    parasites = models.ManyToManyField(Parasite, related_name="examinations", verbose_name=_("pasożyty"), blank=True)
    viruses = models.ManyToManyField(Virus, related_name="examinations", verbose_name=_("wirusy"), blank=True)
    vaccines = models.ManyToManyField(Vaccine, related_name="examinations", verbose_name=_("szczepienia"), blank=True)
    note = models.TextField(_("Notatka"), max_length=1000, blank=True, null=True)

    # histopathological examinations
    collagen_layer_thickening = models.PositiveSmallIntegerField(
        _("pogrubienie warstwy kolagenu u podstawy komórek nabłonka"),
        choices=HISTO_CHOICES,
        null=True,
        blank=True
    )
    increased_intraepithelial_lymphocytes = models.PositiveSmallIntegerField(
        _("zwiększona liczba limfocytów śródnabłonkowych"),
        choices=HISTO_CHOICES,
        null=True,
        blank=True
    )
    lymphocytes_infiltration = models.PositiveSmallIntegerField(
        _("naciek z limfocytów"),
        choices=HISTO_CHOICES,
        null=True,
        blank=True
    )
    plasmocytes_infiltration = models.PositiveSmallIntegerField(
        _("naciek z plazmocytów"),
        choices=HISTO_CHOICES,
        null=True,
        blank=True
    )
    eosinophils_infiltration = models.PositiveSmallIntegerField(
        _("naciek z eozynofili"),
        choices=HISTO_CHOICES,
        null=True,
        blank=True
    )
    mast_cells_infiltration = models.PositiveSmallIntegerField(
        _("naciek z komórek tucznych"),
        choices=HISTO_CHOICES,
        null=True,
        blank=True
    )
    neutrocytes_infiltration = models.PositiveSmallIntegerField(
        _("naciek z neutrocytów"),
        choices=HISTO_CHOICES,
        null=True,
        blank=True
    )

    # TODO: morfologia

    def __str__(self):
        return f"{self.patient} - {self.date}"

    class Meta:
        verbose_name = _("Wywiad medyczny / Badanie"),
        verbose_name_plural = _("Wywiady medyczne / Badania")
