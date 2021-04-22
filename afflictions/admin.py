from django.contrib import admin

from .models import Affliction, Sickness, SicknessExamination, Fungus, FungusExamination, Parasite


class AfflictionAdmin(admin.ModelAdmin):
    list_display = ["name"]


admin.site.register(Affliction, AfflictionAdmin)


class SicknessAdmin(admin.ModelAdmin):
    list_display = ["name"]


class SicknessExaminationInlineAdmin(admin.TabularInline):
    model = SicknessExamination
    extra = 0


admin.site.register(Sickness, SicknessAdmin)


class FungusAdmin(admin.ModelAdmin):
    list_display = ["name", "antibiotics_resistance"]


class FungusExaminationInlineAdmin(admin.TabularInline):
    model = FungusExamination
    extra = 0


admin.site.register(Fungus, FungusAdmin)


class ParasiteAdmin(admin.ModelAdmin):
    list_display = ["species"]


admin.site.register(Parasite, ParasiteAdmin)
