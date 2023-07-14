from django.urls import path
from . import views

urlpatterns = [
    path("school", views.SchoolViewSet.as_view(), name="school_index"),
    path("school/<int:pk>", views.SchoolViewSet.as_view(), name="school_detail"),
    path("course", views.CourseViewSet.as_view(), name="course_index"),
    path("course/<int:pk>", views.CourseViewSet.as_view(), name="course_detail"),
    path("subject", views.SubjectViewSet.as_view(), name="subject_index"),
    path("subject/<int:pk>", views.SubjectViewSet.as_view(), name="subject_detail"),
    path("assignment", views.AssignmentViewSet.as_view(), name="assignment_index"),
    path("assignment/<int:pk>", views.AssignmentViewSet.as_view(), name="assignment_detail"),
    path("assignment/<int:pk>/submit", views.SubmissionViewSet.as_view(), name="submission_index"),
    path("submission/<int:pk>", views.SubmissionViewSet.as_view(), name="submission_index"),
    path("grade", views.GradeViewSet.as_view(), name="subject_index"),
    path("grade/<int:pk>", views.GradeViewSet.as_view(), name="subject_detail"),
]
