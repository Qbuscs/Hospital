from django.urls import path, include

from users.views import UserListView, UserCreateView, ProfileEditView

from .views import (
    AfflictionCreateView,
    AfflictionListView,
    AfflictionDeleteView,
    SicknessCreateView,
    SicknessListView,
    SicknessDeleteView
)


urlpatterns = [
    path("afflictions/", AfflictionListView.as_view(), name="affliction_list"),
    path("afflictions/create", AfflictionCreateView.as_view(), name="affliction_create"),
    path("afflictions/<pk>/delete", AfflictionDeleteView.as_view(), name="affliction_delete"),
    path("sicknesses/", SicknessListView.as_view(), name="sickness_list"),
    path("sicknesses/create", SicknessCreateView.as_view(), name="sickness_create"),
    path("sicknesses/<pk>/delete", SicknessDeleteView.as_view(), name="sickness_delete"),
]
