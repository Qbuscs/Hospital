from django import forms
from django.forms.models import inlineformset_factory

from .models import SicknessExamination, MedicineExamination, FungusExamination, BacteriaExamination
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
    fields=["medicine", "intake_time"], extra=1, can_delete=True
)


class FungusExaminationForm(forms.ModelForm):
    class Meta:
        model = FungusExamination
        fields = "__all__"


FungusExaminationFormSet = inlineformset_factory(
    Examination, FungusExamination, form=FungusExaminationForm,
    fields=["fungus", "amount", "high_resistance", "mid_resistance", "low_resistance"], extra=1, can_delete=True
)


class BacteriaExaminationForm(forms.ModelForm):
    class Meta:
        model = BacteriaExamination
        fields = "__all__"


BacteriaExaminationFormSet = inlineformset_factory(
    Examination, BacteriaExamination, form=BacteriaExaminationForm,
    fields=["bacteria", "high_resistance", "mid_resistance", "low_resistance"], extra=1, can_delete=True
)
