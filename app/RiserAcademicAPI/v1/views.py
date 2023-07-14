from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from RiserAcademicAPI.models import School, Course, Subject, Assignment, Submission, Grade
from .serializers import SchoolSerializer, CourseSerializer, SubjectSerializer,\
    AssignmentSerializer, SubmissionSerializer, GradeSerializer


# Create your views here.
class SchoolViewSet(APIView):
    def get(self, request, pk: int = False):
        try:
            if pk:
                school = School.objects.get(pk=pk)
                serializer = SchoolSerializer(school)
            else:
                schools = School.objects.all()
                serializer = SchoolSerializer(schools, many=True)
            return Response(serializer.data)
        except:
            return Response({
                'error': 'School Does not Exist'
            }, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = SchoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk: int):
        school = School.objects.get(pk=pk)
        serializer = SchoolSerializer(school, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk: int):
        school = School.objects.get(pk=pk)
        school.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CourseViewSet(APIView):
    def get(self, request, pk: int = False):
        try:
            if pk:
                course = Course.objects.get(pk=pk)
                serializer = CourseSerializer(course)
            else:
                course = Course.objects.all()
                serializer = CourseSerializer(course, many=True)
            return Response(serializer.data)
        except:
            return Response({
                'error': 'Course Does not Exist'
            }, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk: int):
        course = Course.objects.get(pk=pk)
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk: int):
        course = Course.objects.get(pk=pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SubjectViewSet(APIView):
    def get(self, request, pk: int = False):
        try:
            if pk:
                subject = Subject.objects.get(pk=pk)
                serializer = SubjectSerializer(subject)
            else:
                subject = Subject.objects.all()
                serializer = SubjectSerializer(subject, many=True)
            return Response(serializer.data)
        except:
            return Response({
                'error': 'Subject Does not Exist'
            }, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk: int):
        subject = Subject.objects.get(pk=pk)
        serializer = SubjectSerializer(subject, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk: int):
        subject = Subject.objects.get(pk=pk)
        subject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AssignmentViewSet(APIView):
    def get(self, request, pk: int = False):
        try:
            if pk:
                assignment = Assignment.objects.get(pk=pk)
                serializer = AssignmentSerializer(assignment)
            else:
                assignment = Assignment.objects.all()
                serializer = AssignmentSerializer(assignment, many=True)
            return Response(serializer.data)
        except:
            return Response({
                'error': 'Assignment Does not Exist'
            }, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = AssignmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk: int):
        assignment = Assignment.objects.get(pk=pk)
        serializer = AssignmentSerializer(assignment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk: int):
        assignment = Assignment.objects.get(pk=pk)
        assignment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SubmissionViewSet(APIView):
    def get(self, request, pk: int = False):
        try:
            if pk:
                submission = Submission.objects.get(pk=pk)
                serializer = SubmissionSerializer(submission)
            else:
                submission = Submission.objects.all()
                serializer = SubmissionSerializer(submission, many=True)
            return Response(serializer.data)
        except:
            return Response({
                'error': 'Submission Does not Exist'
            }, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = SubmissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk: int):
        submission = Submission.objects.get(pk=pk)
        serializer = SubmissionSerializer(submission, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk: int):
        submission = Submission.objects.get(pk=pk)
        submission.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GradeViewSet(APIView):
    def get(self, request, pk: int = False):
        try:
            if pk:
                grade = Grade.objects.get(pk=pk)
                serializer = GradeSerializer(grade)
            else:
                grade = Grade.objects.all()
                serializer = GradeSerializer(grade, many=True)
            return Response(serializer.data)
        except:
            return Response({
                'error': 'Grade Does not Exist'
            }, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = GradeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk: int):
        grade = Grade.objects.get(pk=pk)
        serializer = GradeSerializer(grade, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk: int):
        grade = Grade.objects.get(pk=pk)
        grade.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
