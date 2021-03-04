import debug_toolbar
from django.contrib import admin
from django.urls import path, include

from hospital.views import HomeView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("__debug__/", include(debug_toolbar.urls)),
    path("users/", include("users.urls")),
    path("afflictions/", include("afflictions.urls")),
    path("animals/", include("animals.urls")),
    path("", HomeView.as_view(), name="home"),
    path("", include("core.urls")),
]
