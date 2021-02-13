from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit
from django import forms
from django.utils.translation import gettext_lazy as _
from hospital.layouts import Formset

from .models import Examination


class ExaminationForm(forms.ModelForm):
    class Meta:
        model = Examination
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-md-3 create-label"
        self.helper.field_class = "col-md-9"
        self.helper.layout = Layout(
            Div(
                Field("patient"),
                Field("date"),
                Field("afflictions"),
                Field("parasites"),
                Fieldset(_("Choroby"), Formset("sicknesses")),
                Fieldset(_("Leki"), Formset("medicines")),
                Fieldset(_("Grzyby"), Formset("fungi")),
                Fieldset(_("Kontakty ze zwierzętami"), Formset("animals")),
                Fieldset(_("Podróże"), Formset("travels")),
                #TODO: Rest of fields
                Field("collagen_layer_thickening"),
                Field("increased_intraepithelial_lymphocytes"),
                Field("lymphocytes_infiltration"),
                Field("plasmocytes_infiltration"),
                Field("eosinophils_infiltration"),
                Field("mast_cells_infiltration"),
                Field("neutrocytes_infiltration"),
                Field("note"),
                HTML("<br>"),
                ButtonHolder(Submit("submit", _("Zapisz")))
            )
        )