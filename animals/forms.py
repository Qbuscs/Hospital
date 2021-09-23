from django import forms
from django.forms.models import inlineformset_factory

from .models import AnimalExamination
from core.models import Examination


class AnimalExaminationForm(forms.ModelForm):
    class Meta:
        model = AnimalExamination
        fields = "__all__"


AnimalExaminationFormSet = inlineformset_factory(
    Examination, AnimalExamination, form=AnimalExaminationForm,
    fields=["animal", "contact", "saliva", "excrement", "blood", "scratches", "skin"], extra=1, can_delete=True
)
