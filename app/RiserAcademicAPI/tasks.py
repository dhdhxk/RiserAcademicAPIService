from config.celery import app

from RiserAcademicAPI.models import CourseStudent


@app.task
def add(x, y):
    return x + y


@app.task
def mul(x, y):
    return x * y


def get_course_list_by_student_id(student_id):
    course_list = []
    map_list = CourseStudent.objects.filter(student_id=student_id)
    for mapping in map_list:
        course_list.append(mapping.course_id)
    return course_list
