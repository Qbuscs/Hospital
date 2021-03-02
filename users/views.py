from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, FormView, TemplateView, UpdateView, DeleteView

from users.forms import UserCreateForm, ChangePasswordForm
from users.mixins import AdminMixin

User = get_user_model()


class UserListView(ListView):
    model = User
    template_name = "user_list.html"


class UserCreateView(AdminMixin, CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy("users_list")
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


class UserDeleteView(AdminMixin, DeleteView):
    template_name = "confirm_delete.html"
    model = User
    success_url = reverse_lazy("users_list")


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "profile_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        return context


class ChangePasswordView(LoginRequiredMixin, FormView):
    template_name = "change_password.html"
    form_class = ChangePasswordForm
    success_url = reverse_lazy("profile_detail")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def form_valid(self, form):
        if form.is_valid():
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


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = "profile_edit.html"
    success_url = reverse_lazy("profile_detail")
    fields = ["first_name", "last_name", "username", "email", "phone"]

    def get_object(self, queryset=None):
        return self.request.user

