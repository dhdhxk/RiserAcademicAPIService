from config.celery import app

from RiserAcademicAPI.models import CourseStudent


@app.task
def get_course_list_by_student_id(student_id):
    course_list = []
    map_list = CourseStudent.objects.filter(student_id=student_id)
    for mapping in map_list:
        course_list.append(mapping.course_id)
    return course_list
