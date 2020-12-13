from django.urls import path, include

from users.views import UserListView, UserCreateView


urlpatterns = [
    path("", UserListView.as_view(), name="users_list"),
    path("", include("django.contrib.auth.urls")),
    path("create/", UserCreateView.as_view(), name="user_create"),
]