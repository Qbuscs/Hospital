from django.urls import path

from . import views as affliction_views


urlpatterns = [
    path("afflictions/", affliction_views.AfflictionListView.as_view(), name="affliction_list"),
    path("afflictions/create/", affliction_views.AfflictionCreateView.as_view(), name="affliction_create"),
    path("afflictions/<pk>/delete/", affliction_views.AfflictionDeleteView.as_view(), name="affliction_delete"),

    path("sicknesses/", affliction_views.SicknessListView.as_view(), name="sickness_list"),
    path("sicknesses/<pk>/", affliction_views.SicknessDetailView.as_view(), name="sickness_detail"),
    path("sicknesses/create/", affliction_views.SicknessCreateView.as_view(), name="sickness_create"),
    path("sicknesses/<pk>/delete/", affliction_views.SicknessDeleteView.as_view(), name="sickness_delete"),

    path("medicine/", affliction_views.MedicineListView.as_view(), name="medicine_list"),
    path("medicine/<pk>/", affliction_views.MedicineDetailView.as_view(), name="medicine_detail"),
    path("medicine/create/", affliction_views.MedicineCreateView.as_view(), name="medicine_create"),
    path("medicine/<pk>/delete/", affliction_views.MedicineDeleteView.as_view(), name="medicine_delete"),

    path("parasite/", affliction_views.ParasiteListView.as_view(), name="parasite_list"),
    path("parasite/<pk>/", affliction_views.ParasiteDetailView.as_view(), name="parasite_detail"),
    path("parasite/create/", affliction_views.ParasiteCreateView.as_view(), name="parasite_create"),
    path("parasite/<pk>/delete/", affliction_views.ParasiteDeleteView.as_view(), name="parasite_delete"),
]
