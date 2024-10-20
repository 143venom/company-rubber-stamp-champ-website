from django.urls import path
from .views import *


urlpatterns = [
    path("services/", service_index, name="services"),
    path('services/<int:service_id>/', service_details, name="services-details"),
    path('services/<int:service_id>/delete/', service_delete, name="services-delete"),
]
