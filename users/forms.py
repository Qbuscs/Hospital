from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext

User = get_user_model()


class UserForm(forms.ModelForm):
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
