from django import forms

from .models import Affliction


class AfflictionForm(forms.ModelForm):
    class Meta:
        model = Affliction
