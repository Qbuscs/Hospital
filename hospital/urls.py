import debug_toolbar
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve

from hospital.views import HomeView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("__debug__/", include(debug_toolbar.urls)),
    path("users/", include("users.urls")),
    path("afflictions/", include("afflictions.urls")),
    path("animals/", include("animals.urls")),
    path("morphologies/", include("morphologies.urls")),
    path("", HomeView.as_view(), name="home"),
    path("", include("core.urls")),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]
