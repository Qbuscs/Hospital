from django import forms
from django.forms.models import inlineformset_factory
from django.forms.widgets import TextInput

from .models import Travel
from core.models import Examination


class TravelForm(forms.ModelForm):
    class Meta:
        model = Travel
        fields = "__all__"
        widgets = {
            "date_start": TextInput(attrs={"autocomplete": "off"}),
            "date_end": TextInput(attrs={"autocomplete": "off"}),
        }


TravelFormSet = inlineformset_factory(
    Examination, Travel, form=TravelForm,
    fields=["country", "date_start", "date_end", "food", "drinks", "visit"], extra=1, can_delete=True
)
