from django.urls import path, include

from users.views import UserListView, UserCreateView, UserDeleteView, ProfileView, ChangePasswordView, ProfileUpdateView


urlpatterns = [
    path("", UserListView.as_view(), name="users_list"),
    path("", include("django.contrib.auth.urls")),
    path("create/", UserCreateView.as_view(), name="user_create"),
    path("<pk>/delete/", UserDeleteView.as_view(), name="user_delete"),
    path("profile/", ProfileView.as_view(), name="profile_detail"),
    path("profile/edit", ProfileUpdateView.as_view(), name="profile_edit"),
    path("profile/change_password/", ChangePasswordView.as_view(), name="change_password"),
    path("afflictions/", include("afflictions.urls")),
]
