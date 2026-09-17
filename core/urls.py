from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("api/sample-data/", views.sample_data, name="sample-data"),
    path("api/run-query/", views.run_query, name="run-query"),
]
