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
                Field("afflictions", style="width: 100%"),
                Field("parasites", style="width: 100%"),
                Div(
                    Div(Fieldset(_("Choroby"), Formset("sicknesses")), css_class="card-body"),
                    css_class="card"
                ),
                Div(
                    Div(Fieldset(_("Grzyby"), Formset("fungi")), css_class="card-body"),
                    css_class="card"
                ),
                Div(
                    Div(Fieldset(_("Leki"), Formset("medicines")), css_class="card-body"),
                    css_class="card"
                ),
                Div(
                    Div(Fieldset(_("Kontakty ze zwierzętami"), Formset("animals")), css_class="card-body"),
                    css_class="card"
                ),
                Div(
                    Div(Fieldset(_("Podróże"), Formset("travels")), css_class="card-body table-responsive table-body"),
                    css_class="card"
                ),
                Field("collagen_layer_thickening"),
                Field("increased_intraepithelial_lymphocytes"),
                Field("lymphocytes_infiltration"),
                Field("plasmocytes_infiltration"),
                Field("eosinophils_infiltration"),
                Field("mast_cells_infiltration"),
                Field("neutrocytes_infiltration"),
                Field("note", style="width: 100%"),
                HTML("<br>"),
                ButtonHolder(Submit("submit", _("Zapisz")))
            )
        )