from django.urls import path, include

from users.views import UserListView, UserCreateView, ProfileEditView

from .views import AfflictionCreateView, AfflictionListView, AfflictionDeleteView


urlpatterns = [
    path("afflictions/", AfflictionListView.as_view(), name="afflictions_list"),
    path("afflictions/create", AfflictionCreateView.as_view(), name="afflictions_create"),
    path("afflictions/<pk>/delete", AfflictionDeleteView.as_view(), name="afflictions_delete"),
]
