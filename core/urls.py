from django.urls import path, include

from . import views as core_views


urlpatterns = [
    path("examinations/", core_views.ExaminationListView.as_view(), name="examination_list"),
    path("examinations/create/", core_views.ExaminationCreateView.as_view(), name="examination_create"),
    path("examinations/<pk>/delete/", core_views.ExaminationDeleteView.as_view(), name="examination_delete"),
    path("examinations/<pk>/detail/", core_views.ExaminationDetailView.as_view(), name="examination_detail"),
    path("examinations/<pk>/edit/", core_views.ExaminationUpdateView.as_view(), name="examination_update"),
]
