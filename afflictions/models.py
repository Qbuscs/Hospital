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


class MedicineExamination(models.Model):
    medicine = models.ForeignKey(Medicine, verbose_name=_("lek"), related_name="examinations", on_delete=models.PROTECT)
    examination = models.ForeignKey(
        "core.Examination",
        verbose_name=_("badanie"),
        related_name="medicines",
        on_delete=models.CASCADE
    )
    amount = models.FloatField(_("ilość"), null=True, blank=True)
    # TODO: Może zrobic z tego choice field (mg, tabletek, kropli, itd.)?
    unit = models.CharField(_("jednostka"), null=True, blank=True, max_length=50)

    def __str__(self):
        return str(self.medicine) + f" - {self.amount} {self.unit}"


class SicknessExamination(models.Model):
    sickness = models.ForeignKey(
        Sickness, verbose_name=_("choroba"), related_name="examinations", on_delete=models.PROTECT
    )
    examination = models.ForeignKey(
        "core.Examination", verbose_name=_("badanie"), related_name="sicknesses", on_delete=models.CASCADE
    )
    antibiotics = models.BooleanField(_("Antybiotyko terapia"), null=True, blank=True)

    def __str__(self):
        return str(self.sickness)

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
    afflictions = models.ManyToManyField(
        Affliction,
        verbose_name=_("objawy"),
        related_name="fungi",
        blank=True,
        null=True
    )
    name = models.CharField(_("Nazwa"), max_length=200, null=False, blank=False)
    antibiotics_resistance = models.PositiveSmallIntegerField(
        _("odporność na antybiotyki"),
        choices=ANTIBIOTICS_RESISTANCE_CHOICES
    )

    @classmethod
    def get_antibiotics_resistance_display(val):
        return cls.ANTIBIOTICS_RESISTANCE_CHOICES[val]

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = _("grzyb")
        verbose_name_plural = _("grzyby")


class FungusExamination(models.Model):
    fungus = models.ForeignKey(Fungus, verbose_name=_("grzyb"), related_name="examinations", on_delete=models.PROTECT)
    examination = models.ForeignKey("core.Examination", verbose_name=_("badanie"), related_name="fungi", on_delete=models.CASCADE)
    amount = models.FloatField(_("ilość <#TODO: jaka jednostka?>"))

    def __str__(self):
        return f"{self.fungus} - {self.amount}"

    class Meta:
        verbose_name = _("grzyb w badaniu")
        verbose_name_plural = _("grzyby w badaniu")


class Parasite(models.Model):
    species = models.CharField(_("gatunek"), null=False, blank=False, max_length=200)
    subtype = models.CharField(_("sub-typ"), null=True, blank=True, max_length=200)
    afflictions = models.ManyToManyField(Affliction, verbose_name=_("objawy"), related_name="parasites")

    def __str__(self):
        if self.subtype:
            return f"{self.species} {self.subtype}"
        return f"{self.species}"
    
    class Meta:
        verbose_name = _("pasożyt")
        verbose_name_plural = _("pasożyty")
        unique_together = (("species", "subtype"))
