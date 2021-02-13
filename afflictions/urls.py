from django.urls import path

from . import views as affliction_views


urlpatterns = [
    path("afflictions/", affliction_views.AfflictionListView.as_view(), name="affliction_list"),
    path("afflictions/create/", affliction_views.AfflictionCreateView.as_view(), name="affliction_create"),
    path("afflictions/<pk>/delete/", affliction_views.AfflictionDeleteView.as_view(), name="affliction_delete"),

    path("sicknesses/", affliction_views.SicknessListView.as_view(), name="sickness_list"),
    path("sicknesses/create/", affliction_views.SicknessCreateView.as_view(), name="sickness_create"),
    path("sicknesses/<pk>/", affliction_views.SicknessDetailView.as_view(), name="sickness_detail"),
    path("sicknesses/<pk>/delete/", affliction_views.SicknessDeleteView.as_view(), name="sickness_delete"),

    path("medicines/", affliction_views.MedicineListView.as_view(), name="medicine_list"),
    path("medicines/create/", affliction_views.MedicineCreateView.as_view(), name="medicine_create"),
    path("medicines/<pk>/", affliction_views.MedicineDetailView.as_view(), name="medicine_detail"),
    path("medicines/<pk>/delete/", affliction_views.MedicineDeleteView.as_view(), name="medicine_delete"),

    path("parasites/", affliction_views.ParasiteListView.as_view(), name="parasite_list"),
    path("parasites/create/", affliction_views.ParasiteCreateView.as_view(), name="parasite_create"),
    path("parasites/<pk>/", affliction_views.ParasiteDetailView.as_view(), name="parasite_detail"),
    path("parasites/<pk>/delete/", affliction_views.ParasiteDeleteView.as_view(), name="parasite_delete"),

    path("fungi/", affliction_views.FungusListView.as_view(), name="fungus_list"),
    path("fungi/create/", affliction_views.FungusCreateView.as_view(), name="fungus_create"),
    path("fungi/<pk>/", affliction_views.FungusDetailView.as_view(), name="fungus_detail"),
    path("fungi/<pk>/delete/", affliction_views.FungusDeleteView.as_view(), name="fungus_delete"),
]
