from django import forms
from django.forms.models import inlineformset_factory

from .models import SicknessExamination
from core.models import Examination


class SicknessExaminationForm(forms.ModelForm):
    class Meta:
        model = SicknessExamination


SicknessExaminationFormSet = inlineformset_factory(
    Examination, SicknessExamination, form=SicknessExaminationForm,
    fields=["sickness", "antibiotics"], extra=1, can_delete=True
)
