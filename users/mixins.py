from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.urls import reverse_lazy

User = get_user_model()


class AdminMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse_lazy("login") + f"?next={request.path}")
        if not request.user.role == User.ROLE_ADMIN:
            raise PermissionDenied
        return super().dispatch(request, args, kwargs)


class DoctorMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse_lazy("login") + f"?next={request.path}")
        if not request.user.role == User.ROLE_DOCTOR:
            raise PermissionDenied
        return super().dispatch(request, args, kwargs)


class InternMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse_lazy("login") + f"?next={request.path}")
        if request.user.role not in [User.ROLE_DOCTOR, User.ROLE_INTERN]:
            raise PermissionDenied
        return super().dispatch(request, args, kwargs)
