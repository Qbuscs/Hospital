from django import forms
from django.forms.models import inlineformset_factory

from .models import SicknessExamination, MedicineExamination, FungusExamination
from core.models import Examination


class SicknessExaminationForm(forms.ModelForm):
    class Meta:
        model = SicknessExamination
        fields = "__all__"


SicknessExaminationFormSet = inlineformset_factory(
    Examination, SicknessExamination, form=SicknessExaminationForm,
    fields=["sickness", "antibiotics"], extra=1, can_delete=True
)


class MedicineExaminationForm(forms.ModelForm):
    class Meta:
        model = MedicineExamination
        fields = "__all__"


MedicineExaminationFormSet = inlineformset_factory(
    Examination, MedicineExamination, form=MedicineExaminationForm,
    fields=["medicine", "amount", "unit"], extra=1, can_delete=True
)


class FungusExaminationForm(forms.ModelForm):
    class Meta:
        model = FungusExamination
        fields = "__all__"


FungusExaminationFormSet = inlineformset_factory(
    Examination, FungusExamination, form=FungusExaminationForm,
    fields=["fungus", "amount"], extra=1, can_delete=True
)
