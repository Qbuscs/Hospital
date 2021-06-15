from django import forms
from django.forms.models import inlineformset_factory
from django.forms.widgets import TextInput, DateInput

from .models import Travel
from core.models import Examination


class TravelForm(forms.ModelForm):
    class Meta:
        model = Travel
        fields = "__all__"
        widgets = {
            "date_start": DateInput(attrs={"autocomplete": "off"}),
            "date_end": DateInput(attrs={"autocomplete": "off"}),
        }


TravelFormSet = inlineformset_factory(
    Examination, Travel, form=TravelForm,
    fields=["country", "date_start", "date_end", "food", "drinks", "visit", "specialist_advice", "specificity"], extra=1, can_delete=True
)
