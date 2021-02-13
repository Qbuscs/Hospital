from django import forms
from django.forms.models import inlineformset_factory

from .models import Travel
from core.models import Examination


class TravelForm(forms.ModelForm):
    class Meta:
        model = Travel
        fields = "__all__"


TravelFormSet = inlineformset_factory(
    Examination, Travel, form=TravelForm,
    fields=["country", "date_start", "date_end", "food", "drinks", "visit"], extra=1, can_delete=True
)
