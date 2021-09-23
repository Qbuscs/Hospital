from django.contrib import admin

from afflictions.admin import SicknessExaminationInlineAdmin, FungusExaminationInlineAdmin
from animals.admin import AnimalExaminationAdmin
from travels.admin import TravelInlineAdmin
from .models import Examination


class ExaminationAdmin(admin.ModelAdmin):
    list_display = ['date']
    inlines = [
        AnimalExaminationAdmin,
        TravelInlineAdmin,
        SicknessExaminationInlineAdmin,
        FungusExaminationInlineAdmin
    ]


admin.site.register(Examination, ExaminationAdmin)