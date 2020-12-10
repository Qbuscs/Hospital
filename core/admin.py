from django.contrib import admin

from afflictions.admin import SicknessExaminationInlineAdmin, FungusExaminationInlineAdmin
from animals.admin import AnimalExaminationAdmin
from travels.admin import TravelInlineAdmin
from .models import Patient, Examination


class PatientAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name"]


class ExaminationAdmin(admin.ModelAdmin):
    list_display = ['patient', 'date']
    inlines = [
        AnimalExaminationAdmin,
        TravelInlineAdmin,
        SicknessExaminationInlineAdmin,
        FungusExaminationInlineAdmin
    ]


admin.site.register(Patient, PatientAdmin)
admin.site.register(Examination, ExaminationAdmin)