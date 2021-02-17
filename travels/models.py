from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField

from core.models import Examination


class Travel(models.Model):
    FOOD_RESTAURANTS = 0
    FOOD_LOCAL = 1
    FOOD_OWN = 2
    FOOD_MIXED = 3

    FOOD_CHOICES = (
        (FOOD_RESTAURANTS, _("restauracje")),
        (FOOD_LOCAL, _("lokalne")),
        (FOOD_OWN, _("własne")),
        (FOOD_MIXED, _("mieszane")),
    )

    DRINKS_BOTTLED = 0
    DRINKS_LOCAL = 1
    DRINKS_STREAM = 2
    DRINKS_MIXED = 3

    DRINKS_CHOICES = (
        (DRINKS_BOTTLED, _("butelkowane")),
        (DRINKS_LOCAL, _("lokalne")),
        (DRINKS_STREAM, _("strumienie")),
        (DRINKS_MIXED, _("mieszane")),
    )

    VISIT_PROFESSIONAL = 0
    VISIT_TOURISTIC = 1

    VISIT_CHOICES = (
        (VISIT_PROFESSIONAL, _("zawodowy")),
        (VISIT_TOURISTIC, _("turystyczny")),
    )

    examination = models.ForeignKey(Examination, related_name="travels", on_delete=models.CASCADE, null=False)
    country = CountryField(_("kraj"), null=False, blank=False)
    date_start = models.DateField(_("początek"), null=False)
    date_end = models.DateField(_("koniec"), null=False)
    food = models.PositiveSmallIntegerField(_("odżywianie"), choices=FOOD_CHOICES, null=True)
    drinks = models.PositiveSmallIntegerField(_("napoje"), choices=DRINKS_CHOICES, null=True)
    visit = models.PositiveSmallIntegerField(_("rodzaj wizyty"), choices=VISIT_CHOICES, null=True)

    class Meta:
        verbose_name = _("podróż")
        verbose_name_plural = _("podróże")
