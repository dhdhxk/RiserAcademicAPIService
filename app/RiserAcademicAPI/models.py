from django.db import models


# Create your models here.
class School(models.Model):
    school_id = models.BigAutoField(primary_key=True)
    school_name = models.CharField(max_length=30)
    school_type = models.CharField(max_length=1)
    school_city = models.CharField(max_length=30)
    school_state = models.CharField(max_length=30)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.school_name

    def get_absolute_url(self):
        return f'/school/{self.id}'


class Course(models.Model):
    course_id = models.BigAutoField(primary_key=True)
    course_code = models.CharField(max_length=30)
    course_name = models.CharField(max_length=255)
    course_room = models.CharField(max_length=30)
    is_deleted = models.BooleanField(default=False)
    school = models.ForeignKey(School, db_constraint=False, on_delete=models.DO_NOTHING, related_name='courses')
    teacher_id = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course_name

    def get_absolute_url(self):
        return f'/class/{self.id}'


class CourseStudent(models.Model):
    class Meta:
        db_table = 'RiserAcademicAPI_course_student'

    id = models.BigAutoField(primary_key=True)
    student_id = models.BigIntegerField()
    course = models.ForeignKey(School, db_constraint=False, on_delete=models.DO_NOTHING, related_name='course_student')


class Subject(models.Model):
    subject_id = models.BigAutoField(primary_key=True)
    subject_name = models.CharField(max_length=255)
    subject_level = models.CharField(max_length=30)
    is_deleted = models.BooleanField(default=False)
    course = models.ManyToManyField(Course, related_name="subjects")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject_name


class Assignment(models.Model):
    assignment_id = models.BigAutoField(primary_key=True)

    VARIABLE_NAME = (  # This should be capital
        ('a', 'Assignment'),
        ('q', 'Quiz'),
        ('t', 'Test')
    )
    assignment_type = models.CharField(max_length=1, choices=VARIABLE_NAME)
    assignment_name = models.CharField(max_length=30)
    assignment_total_score = models.CharField(max_length=30)
    assignment_point = models.CharField(max_length=30)
    assignment_contents = models.TextField(max_length=3000)
    is_deleted = models.BooleanField(default=False)
    course = models.ForeignKey(Course, db_constraint=False, on_delete=models.DO_NOTHING, blank=True,
                               null=True, related_name='assignments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.assignment_name


class Submission(models.Model):
    submission_id = models.BigAutoField(primary_key=True)
    submission_score = models.CharField(max_length=30)
    is_deleted = models.BooleanField(default=False)
    assignment = models.ForeignKey(Assignment, db_constraint=False, on_delete=models.DO_NOTHING, blank=True,
                                   null=True, related_name='submissions')
    student_id = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.submission_id}: {self.submission_score}"


class Grade(models.Model):
    grade_id = models.BigAutoField(primary_key=True)
    grade_score = models.CharField(max_length=30)
    is_deleted = models.BooleanField(default=False)
    course = models.ForeignKey(Course, db_constraint=False, on_delete=models.DO_NOTHING, blank=True,
                               null=True, related_name='grades')
    student_id = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.grade_id}: {self.grade_score}"
