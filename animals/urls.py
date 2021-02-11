from django.urls import path

from . import views as animal_views


urlpatterns = [
    path("animals/", animal_views.AnimalListView.as_view(), name="animal_list"),
    path("animals/create/", animal_views.AnimalCreateView.as_view(), name="animal_create"),
    path("animals/<pk>/delete/", animal_views.AnimalDeleteView.as_view(), name="animal_delete"),
]
