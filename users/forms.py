from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils.translation import gettext

User = get_user_model()


class UserCreateForm(forms.ModelForm):
    username = forms.CharField(max_length=30, required=True, label=gettext("Login"))
    first_name = forms.CharField(max_length=30, required=True, label=gettext("Imię"))
    last_name = forms.CharField(max_length=30, required=True, label=gettext("Nazwisko"))
    role = forms.ChoiceField(choices=User.ROLE_CHOICES, required=True, label=gettext("Rola"))
    password = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(), label=gettext("Hasło"))

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "role",
            "password",
        ]


class ProfileEditForm(forms.ModelForm):
    password1 = forms.CharField(
        max_length=50, required=True, widget=forms.PasswordInput(), label=gettext("Nowe hasło")
    )
    password2 = forms.CharField(
        max_length=50, required=True, widget=forms.PasswordInput(), label=gettext("Powtórz hasło")
    )

    class Meta:
        model = User
        fields = [
            "password1",
            "password2"
        ]
    
    def clean_password2(self):
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]
        if not password1 == password2:
            raise ValidationError(gettext("Wprowadzone hasła różnią się od siebie"), code="invalid")
