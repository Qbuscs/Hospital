from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.translation import gettext


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
    intake_time = models.PositiveIntegerField(_("Czas przyjmowania (tygodnie)"), null=True, blank=True)

    def __str__(self):
        days = self.intake_time if self.intake_time else "???"
        return str(self.medicine) + f" - {days} " + gettext("dni") 


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
    afflictions = models.ManyToManyField(
        Affliction,
        verbose_name=_("objawy"),
        related_name="fungi",
        blank=True,
    )
    name = models.CharField(_("Nazwa"), max_length=200, null=False, blank=False)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = _("grzyb")
        verbose_name_plural = _("grzyby")


class FungusExamination(models.Model):
    fungus = models.ForeignKey(Fungus, verbose_name=_("grzyb"), related_name="examinations", on_delete=models.PROTECT)
    examination = models.ForeignKey(
        "core.Examination",
        verbose_name=_("badanie"),
        related_name="fungi",
        on_delete=models.CASCADE
    )
    amount = models.FloatField(_("ilość"))
    high_resistance = models.ManyToManyField(
        Medicine,
        verbose_name=_("oporny na"),
        related_name="examinations_fungi_high_resistance",
        blank=True
    )
    mid_resistance = models.ManyToManyField(
        Medicine,
        verbose_name=_("średnio wrażliwy na"),
        related_name="examinations_fungi_mid_resistance",
        blank=True
    )
    low_resistance = models.ManyToManyField(
        Medicine,
        verbose_name=_("wrażliwy na"),
        related_name="examinations_fungi_low_resistance",
        blank=True
    )

    def __str__(self):
        return f"{self.fungus} ({self.amount})"

    class Meta:
        verbose_name = _("grzyb w badaniu")
        verbose_name_plural = _("grzyby w badaniu")


class Parasite(models.Model):
    species = models.CharField(_("gatunek"), null=False, blank=False, max_length=200)
    subtype = models.CharField(_("sub-typ"), null=True, blank=True, max_length=200)
    afflictions = models.ManyToManyField(
        Affliction, verbose_name=_("objawy"), related_name="parasites", null=True, blank=True
    )

    def __str__(self):
        if self.subtype:
            return f"{self.species} {self.subtype}"
        return f"{self.species}"
    
    class Meta:
        verbose_name = _("pasożyt")
        verbose_name_plural = _("pasożyty")
        unique_together = (("species", "subtype"))


class Bacteria(models.Model):
    name = models.CharField(_("Gatunek"), max_length=200, null=False, blank=False)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = _("bakteria")
        verbose_name_plural = _("bakterie")


class BacteriaExamination(models.Model):
    bacteria = models.ForeignKey(
        Bacteria,
        verbose_name=_("bakteria"),
        related_name="examinations",
        on_delete=models.PROTECT
    )
    examination = models.ForeignKey(
        "core.Examination",
        verbose_name=_("badanie"),
        related_name="bacteria",
        on_delete=models.CASCADE
    )
    high_resistance = models.ManyToManyField(
        Medicine,
        verbose_name=_("oporny na"),
        related_name="examination_bacteria_high_resistance",
        blank=True
    )
    mid_resistance = models.ManyToManyField(
        Medicine,
        verbose_name=_("średnio wrażliwy na"),
        related_name="examination_bacteria_mid_resistance",
        blank=True
    )
    low_resistance = models.ManyToManyField(
        Medicine,
        verbose_name=_("wrażliwy na"),
        related_name="examination_bacteria_low_resistance",
        blank=True
    )

    def __str__(self):
        return f"{self.bacteria}"

    class Meta:
        verbose_name = _("bakteria w badaniu")
        verbose_name_plural = _("bakterie w badaniu")


class Virus(models.Model):
    name = models.CharField(_("Gatunek"), max_length=200, null=False, blank=False)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = _("wirus")
        verbose_name_plural = _("wirus")
