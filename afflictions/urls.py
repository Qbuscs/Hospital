from django.urls import path

from .views import affliction_views, fungus_views, medicine_views, parasite_views, sickness_views


urlpatterns = [
    path("afflictions/", affliction_views.AfflictionListView.as_view(), name="affliction_list"),
    path("afflictions/create/", affliction_views.AfflictionCreateView.as_view(), name="affliction_create"),
    path("afflictions/<pk>/delete/", affliction_views.AfflictionDeleteView.as_view(), name="affliction_delete"),
    path("afflictions/<pk>/edit/", affliction_views.AfflictionUpdateView.as_view(), name="affliction_update"),

    path("sicknesses/", sickness_views.SicknessListView.as_view(), name="sickness_list"),
    path("sicknesses/create/", sickness_views.SicknessCreateView.as_view(), name="sickness_create"),
    path("sicknesses/<pk>/", sickness_views.SicknessDetailView.as_view(), name="sickness_detail"),
    path("sicknesses/<pk>/delete/", sickness_views.SicknessDeleteView.as_view(), name="sickness_delete"),
    path("sicknesses/<pk>/edit/", sickness_views.SicknessUpdateView.as_view(), name="sickness_update"),

    path("medicines/", medicine_views.MedicineListView.as_view(), name="medicine_list"),
    path("medicines/create/", medicine_views.MedicineCreateView.as_view(), name="medicine_create"),
    path("medicines/<pk>/", medicine_views.MedicineDetailView.as_view(), name="medicine_detail"),
    path("medicines/<pk>/delete/", medicine_views.MedicineDeleteView.as_view(), name="medicine_delete"),
    path("medicines/<pk>/edit/", medicine_views.MedicineUpdateView.as_view(), name="medicine_update"),

    path("parasites/", parasite_views.ParasiteListView.as_view(), name="parasite_list"),
    path("parasites/create/", parasite_views.ParasiteCreateView.as_view(), name="parasite_create"),
    path("parasites/<pk>/", parasite_views.ParasiteDetailView.as_view(), name="parasite_detail"),
    path("parasites/<pk>/delete/", parasite_views.ParasiteDeleteView.as_view(), name="parasite_delete"),
    path("parasites/<pk>/edit/", parasite_views.ParasiteUpdateView.as_view(), name="parasite_update"),

    path("fungi/", fungus_views.FungusListView.as_view(), name="fungus_list"),
    path("fungi/create/", fungus_views.FungusCreateView.as_view(), name="fungus_create"),
    path("fungi/<pk>/", fungus_views.FungusDetailView.as_view(), name="fungus_detail"),
    path("fungi/<pk>/delete/", fungus_views.FungusDeleteView.as_view(), name="fungus_delete"),
    path("fungi/<pk>/edit/", fungus_views.FungusUpdateView.as_view(), name="fungus_update"),
]
