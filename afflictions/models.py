from django.db import models
from django.utils.translation import gettext_lazy as _


class Affliction(models.Model):
    name = models.CharField(_("nazwa"), max_length=200, null=False, blank=False)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = _("objaw")
        verbose_name_plural = _("objawy")


class Sickness(models.Model):
    name = models.CharField(_("nazwa"), max_length=200, null=False, blank=False)
    afflictions = models.ManyToManyField(Affliction, related_name="sicknesses", verbose_name=_("objawy"))

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = _("choroba"),
        verbose_name_plural = _("choroby")


class Medicine(models.Model):
    name = models.CharField(_("nazwa"), max_length=200, null=False, blank=False)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = _("lek"),
        verbose_name_plural = _("leki")


# TODO: class MedicineSicknessExamination(models.Model)


class SicknessExamination(models.Model):
    sickness = models.ForeignKey(Sickness, verbose_name=_("choroba"), on_delete=models.PROTECT)
    examination = models.ForeignKey("core.Examination", verbose_name=_("badanie"), on_delete=models.CASCADE)
    antibiotics = models.BooleanField(_("Antybiotyko terapia"), null=True, blank=True)

    class Meta:
        verbose_name = _("Choroba w badaniu")
        verbose_name_plural = _("Choroby w badaniu")


class Fungus(models.Model):
    ANTIBIOTICS_RESISTANCE_LOW = 0
    ANTIBIOTICS_RESISTANCE_MEDIUM = 1
    ANTIBIOTICS_RESISTANCE_HIGH = 2

    ANTIBIOTICS_RESISTANCE_CHOICES = (
        (ANTIBIOTICS_RESISTANCE_LOW, _("niska")),
        (ANTIBIOTICS_RESISTANCE_MEDIUM, _("średnia")),
        (ANTIBIOTICS_RESISTANCE_HIGH, _("wysoka")),
    )

    # TODO: hodowla
    # TODO: gatunek
    # TODO: genotyp
    afflictions = models.ManyToManyField(Affliction, verbose_name=_("objawy"), related_name="fungi")
    molecular_identification = models.TextField(_("identyfikacja molekularna"), null=False, blank=False)
    antibiotics_resistance = models.PositiveSmallIntegerField(
        _("odporność na antybiotyki"),
        choices=ANTIBIOTICS_RESISTANCE_CHOICES
    )

    def __str__(self):
        return f"{self.molecular_identification}"

    class Meta:
        verbose_name = _("grzyb")
        verbose_name_plural = _("grzyby")


class FungusExamination(models.Model):
    fungus = models.ForeignKey(Fungus, verbose_name=_("grzyb"), on_delete=models.PROTECT)
    examination = models.ForeignKey("core.Examination", verbose_name=_("badanie"), on_delete=models.CASCADE)
    amount = models.FloatField(_("ilość"))

    class Meta:
        verbose_name = _("grzyb w badaniu")
        verbose_name_plural = _("grzyby w badaniu")


class Parasite(models.Model):
    name = models.CharField(_("nazwa"), null=False, blank=False, max_length=200)
    afflictions = models.ManyToManyField(Affliction, verbose_name=_("objawy"), related_name="parasites")

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = _("pasożyt")
        verbose_name_plural = _("pasożyty")