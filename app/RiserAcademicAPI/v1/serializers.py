from rest_framework import serializers
from RiserAcademicAPI.models import Course, School, Subject, Assignment, Submission, Grade


class SchoolSerializer(serializers.ModelSerializer):
    courses = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=False,
        queryset=Course.objects.all()
    )

    class Meta:
        model = School
        fields = ['school_id', 'school_name', 'school_type', 'school_city', 'school_state', 'courses', 'is_deleted',
                  'created_at', 'updated_at']


class CourseSerializer(serializers.ModelSerializer):
    subjects = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=False,
        queryset=Subject.objects.all()
    )
    assignments = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=False,
        queryset=Assignment.objects.all()
    )
    grades = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=False,
        queryset=Grade.objects.all()
    )

    class Meta:
        model = Course
        fields = ['course_id', 'course_code', 'course_name', 'course_room', 'is_deleted', 'subjects', 'assignments',
                  'grades', 'teacher_id', 'created_at', 'updated_at']


class SubjectSerializer(serializers.ModelSerializer):
    courses = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=False,
        queryset=Course.objects.all()
    )

    class Meta:
        model = Subject
        fields = ['subject_id', 'subject_name', 'subject_level', 'courses', 'is_deleted', 'created_at', 'updated_at']


class AssignmentSerializer(serializers.ModelSerializer):
    submissions = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=False,
        queryset=Submission.objects.all()
    )

    class Meta:
        model = Assignment
        fields = ['assignment_id', 'assignment_type', 'assignment_name', 'assignment_total_score', 'assignment_point',
                  'assignment_contents', 'submissions', 'is_deleted', 'created_at', 'updated_at']


class SubmissionSerializer(serializers.ModelSerializer):
    courses = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=False,
        queryset=Course.objects.all()
    )

    class Meta:
        model = Submission
        fields = ['submission_id', 'submission_score', 'student_id', 'is_deleted', 'created_at', 'updated_at']


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ['grade_id', 'grade_score', 'is_deleted', 'student_id', 'created_at', 'updated_at']
