from django.urls import path, include

from . import views as core_views


urlpatterns = [
    path("patients/", core_views.PatientListView.as_view(), name="patient_list"),
    path("patients/create/", core_views.PatientCreateView.as_view(), name="patient_create"),
    path("patients/<pk>/delete/", core_views.PatientDeleteView.as_view(), name="patient_delete"),
]
