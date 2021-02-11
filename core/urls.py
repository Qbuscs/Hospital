from django.urls import path, include

from . import views as core_views


urlpatterns = [
    path("patients/", core_views.PatientListView.as_view(), name="patient_list"),
    path("patients/create/", core_views.PatientCreateView.as_view(), name="patient_create"),
    path("patients/<pk>/delete/", core_views.PatientDeleteView.as_view(), name="patient_delete"),

    path("examinations/", core_views.ExaminationListView.as_view(), name="examination_list"),
    path("examinations/create/", core_views.ExaminationCreateView.as_view(), name="examination_create"),
    path("examinations/<pk>/delete/", core_views.ExaminationDeleteView.as_view(), name="examination_delete"),
    path("examinations/<pk>/detail/", core_views.ExaminationDetailView.as_view(), name="examination_detail"),
]
