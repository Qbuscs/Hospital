from django.db import models
from django.utils.translation import gettext_lazy as _


class Animal(models.Model):
    name = models.CharField(_("nazwa"), null=False, blank=False, max_length=200)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = _("zwierzę")
        verbose_name_plural = _("zwierzęta")


class AnimalExamination(models.Model):
    CONTACT_PROFESSIONAL = 0
    CONTACT_DOMESTIC = 1
    CONTACT_OTHER = 2

    CONTACT_CHOICES = (
        (CONTACT_PROFESSIONAL, _("zawodowe")),
        (CONTACT_DOMESTIC, _("domowe")),
        (CONTACT_OTHER, _("inne"))
    )

    animal = models.ForeignKey(Animal, verbose_name=_("zwierzę"), on_delete=models.CASCADE)
    examination = models.ForeignKey("core.Examination", on_delete=models.CASCADE)
    contact = models.PositiveSmallIntegerField(_("kontakt"), choices=CONTACT_CHOICES)
    saliva = models.BooleanField(_("kontakt ze śliną"), null=True, blank=True)
    excrement = models.BooleanField(_("kontakt z odchodami"), null=True, blank=True)

    class Meta:
        verbose_name = _("Kontakt ze zwierzęciem")
        verbose_name_plural = _("Kontakty ze zwierzętami")
