from django.contrib import admin

from .models import Animal, AnimalExamination


class AnimalExaminationAdmin(admin.TabularInline):
    model = AnimalExamination
    extra = 0


class AnimalAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Animal, AnimalAdmin)
