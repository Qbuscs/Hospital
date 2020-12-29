from django.urls import path, include

from users.views import UserListView, UserCreateView, ProfileEditView


urlpatterns = [
    path("", UserListView.as_view(), name="users_list"),
    path("", include("django.contrib.auth.urls")),
    path("create/", UserCreateView.as_view(), name="user_create"),
    path("profile/", ProfileEditView.as_view(), name="profile_edit"),
    path("afflictions/", include("afflictions.urls")),
]
