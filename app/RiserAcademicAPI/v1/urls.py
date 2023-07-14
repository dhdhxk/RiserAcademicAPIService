from django.urls import path
from . import views

urlpatterns = [
    path("school", views.SchoolViewSet.as_view(), name="school_index"),
    path("school/<int:pk>", views.SchoolViewSet.as_view(), name="school_detail"),
    path("course", views.CourseViewSet.as_view(), name="course_index"),
    path("course/<int:pk>", views.CourseViewSet.as_view(), name="course_detail"),
    path("subject", views.SubjectViewSet.as_view(), name="subject_index"),
    path("subject/<int:pk>", views.SubjectViewSet.as_view(), name="subject_detail"),
]
