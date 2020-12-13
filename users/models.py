from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    ROLE_ADMIN = 0
    ROLE_DOCTOR = 1
    ROLE_INTERN = 2

    ROLE_CHOICES = (
        (ROLE_ADMIN, _("Admin")),
        (ROLE_DOCTOR, _("Lekarz")),
        (ROLE_INTERN, _("Praktykant")),
    )

    role = models.PositiveSmallIntegerField(
        _("rola"), choices=ROLE_CHOICES, blank=False, null=False, default=ROLE_ADMIN
    )

    def __str__(self):
        return self.username
