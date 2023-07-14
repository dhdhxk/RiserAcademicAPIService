from django.urls import path, include

urlpatterns = [
    path("v1/", include("RiserAcademicAPI.v1.urls")),
]
