from django import forms
from django.forms.models import inlineformset_factory

from .models import MorphologyExamination
from core.models import Examination


class MorphologyExaminationForm(forms.ModelForm):
    class Meta:
        model = MorphologyExamination
        fields = "__all__"


MorphologyExaminationFormSet = inlineformset_factory(
    Examination, MorphologyExamination, form=MorphologyExaminationForm,
    fields=["morphology", "value"], extra=1, can_delete=True
)
