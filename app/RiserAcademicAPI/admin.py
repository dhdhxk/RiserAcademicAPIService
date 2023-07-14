from django.contrib import admin

from .models import School, Course, Subject, Assignment, Submission, Grade


# Register your models here.
class SchoolClass(admin.ModelAdmin):
    fields = ['school_name', 'school_type', 'school_city', 'school_state', 'is_deleted']


admin.site.register(School, SchoolClass)


class CourseClass(admin.ModelAdmin):
    fields = ['course_code', 'course_name', 'course_room', 'school', 'is_deleted']


admin.site.register(Course, CourseClass)


class SubjectClass(admin.ModelAdmin):
    fields = ['subject_name', 'subject_level', 'course', 'is_deleted']


admin.site.register(Subject, SubjectClass)


class AssignmentClass(admin.ModelAdmin):
    fields = ['assignment_type', 'assignment_name', 'assignment_total_score', 'assignment_point',
              'assignment_contents', 'course', 'is_deleted']


admin.site.register(Assignment, AssignmentClass)


class SubmissionClass(admin.ModelAdmin):
    fields = ['submission_score', 'is_deleted']


admin.site.register(Submission, SubmissionClass)


class GradeClass(admin.ModelAdmin):
    fields = ['grade_score', 'course', 'is_deleted']


admin.site.register(Grade, GradeClass)
