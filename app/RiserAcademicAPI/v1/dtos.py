from djantic import ModelSchema
from models import School, Course, Subject, Assignment, Submission, Grade


class SchoolDTO(ModelSchema):
    class Config:
        model = School


class CourseDTO(ModelSchema):
    class Config:
        model = Course


class SubjectDTO(ModelSchema):
    class Config:
        model = Subject


class AssignmentDTO(ModelSchema):
    class Config:
        model = Assignment


class SubmissionDTO(ModelSchema):
    class Config:
        model = Submission


class GradeDTO(ModelSchema):
    class Config:
        model = Grade
