from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, FormView

from users.forms import UserCreateForm, ProfileEditForm
from users.mixins import AdminMixin

User = get_user_model()


class UserListView(ListView):
    model = User
    template_name = "user_list.html"


class UserCreateView(AdminMixin, CreateView):
    form_class = UserCreateForm
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
            return super().form_valid()


class ProfileEditView(LoginRequiredMixin, FormView):
    form_class = ProfileEditForm
    success_url = reverse_lazy("login")
    template_name = "profile_edit.html"

    def form_valid(self, form):
        if form.is_valid:
            password = form.cleaned_data.pop("password1")
            self.request.user.set_password(password)
            self.request.user.save()
            return redirect(self.success_url)
        else:
            return super().form_valid()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        return context
