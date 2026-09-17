from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("api/sample-data/", views.sample_data, name="sample-data"),
]
