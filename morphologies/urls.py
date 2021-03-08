from django.urls import path

from .views import (MorphologyCreateView, MorphologyDeleteView,
                    MorphologyListView, MorphologyUpdateView)

urlpatterns = [
    path("", MorphologyListView.as_view(), name="morphology_list"),
    path("create/", MorphologyCreateView.as_view(), name="morphology_create"),
    path("<pk>/delete/", MorphologyDeleteView.as_view(), name="morphology_delete"),
    path("<pk>/edit/", MorphologyUpdateView.as_view(), name="morphology_update"),
]
