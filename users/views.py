from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from users.forms import UserForm
from users.mixins import AdminMixin

User = get_user_model()


class UserListView(ListView):
    model = User
    template_name = "user_list.html"


class UserCreateView(AdminMixin, CreateView):
    form_class = UserForm
    success_url = reverse_lazy("user_create")
    template_name = "user_create.html"

    def form_valid(self, form):
        if form.is_valid:
            password = form.cleaned_data.pop("password")
            user = User.objects.create(**form.cleaned_data)
            user.set_password(password)
            user.save()
            return redirect(self.success_url + "?success")
        else:
            print("invalid")
            return super().form_valid()
