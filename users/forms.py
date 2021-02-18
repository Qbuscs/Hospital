from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils.translation import gettext
from phonenumber_field.formfields import PhoneNumberField

User = get_user_model()


class UserCreateForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True, label=gettext("Login"))
    role = forms.ChoiceField(choices=User.ROLE_CHOICES, required=True, label=gettext("Rola"))
    first_name = forms.CharField(max_length=30, required=True, label=gettext("Imię"))
    last_name = forms.CharField(max_length=30, required=True, label=gettext("Nazwisko"))
    email = forms.CharField(max_length=50, required=False, label=gettext("E-mail"))
    phone = PhoneNumberField(required=False, label=gettext("Nr telefonu"))
    password = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(), label=gettext("Hasło"))

    class Meta:
        model = User
        fields = [
            "username",
            "role",
            "first_name",
            "last_name",
            "email",
            "phone",   
            "password",
        ]


class ChangePasswordForm(forms.ModelForm):
    password_current = password1 = forms.CharField(
        max_length=50, required=True, widget=forms.PasswordInput(), label=gettext("Aktualne hasło")
    )
    password1 = forms.CharField(
        max_length=50, required=True, widget=forms.PasswordInput(), label=gettext("Nowe hasło")
    )
    password2 = forms.CharField(
        max_length=50, required=True, widget=forms.PasswordInput(), label=gettext("Powtórz hasło")
    )

    class Meta:
        model = User
        fields = [
            "password_current",
            "password1",
            "password2"
        ]

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def clean_password_current(self):
        password = self.cleaned_data["password_current"]
        if not self.user.check_password(password):
            raise ValidationError(gettext("Podano błędne aktualne hasło"), code="invalid")

    def clean_password2(self):
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]
        if not password1 == password2:
            raise ValidationError(gettext("Wprowadzone hasła różnią się od siebie"), code="invalid")
