from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import Examination


class Morphology(models.Model):
    name = models.CharField(_("Nazwa"), max_length=64)
    unit = models.CharField(_("Jednostka"), max_length=32)
    norm_min = models.FloatField(_("Norma dolna"), null=True, blank=True)
    norm_max = models.FloatField(_("Norma górna"), null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.norm_min}-{self.norm_max} {self.unit})"

    class Meta:
        verbose_name = _("Badanie morfologiczne")
        verbose_name_plural = _("Badania morfologiczne")


class MorphologyExamination(models.Model):
    MORPHOLOGY_LOW = 0
    MORPHOLOGY_NORMAL = 1
    MORPHOLOGY_HIGH = 2

    morphology = models.ForeignKey(Morphology, verbose_name=_("Badanie morfologiczne"), on_delete=models.PROTECT)
    examination = models.ForeignKey(
        Examination, related_name="morphologies", verbose_name=_("Badanie"), on_delete=models.CASCADE
    )
    value = models.FloatField(_("Wyniki"))

    def norm(self):
        if self.value < self.morphology.norm_min:
            return MorphologyExamination.MORPHOLOGY_LOW
        if self.value > self.morphology.norm_max:
            return MorphologyExamination.MORPHOLOGY_HIGH
        return MorphologyExamination.MORPHOLOGY_NORMAL
    
    def norm_str(self):
        morphology_text = {
            MorphologyExamination.MORPHOLOGY_LOW: _("Poniżej normy"),
            MorphologyExamination.MORPHOLOGY_NORMAL: _("W normie"),
            MorphologyExamination.MORPHOLOGY_HIGH: _("Powyżej normy"),
        }
        return morphology_text[self.norm()]
    
    def __str__(self):
        return f"{self.morphology.name} - {self.value} {self.morphology.unit} ({self.norm_str()})"

    class Meta:
        unique_together = ("morphology", "examination")
        verbose_name = _("Wynik morfologii")
        verbose_name_plural = _("Wyniki morfologii")
