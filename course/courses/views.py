from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from .services import (
    create_course,
    update_course,
    delete_course,
    get_all_courses,
    get_course_by_id
)
from .serializers import CourseSerializer
from .models import Course
from utils.permissions import RolePermissionFactory

class CourseListView(APIView):
    print("CourseCourseListView")
    def get(self, request):
        courses = get_all_courses()
        print("courses", courses)
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CourseCreateView(APIView):
    def post(self, request):
        try:
            course = create_course(request.data)
            return Response(CourseSerializer(course).data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({"errors": e.detail}, status=status.HTTP_400_BAD_REQUEST)

class CourseDetailView(APIView):
    def get(self, request, course_id):
        try:
            course = get_course_by_id(course_id)
            return Response(course, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"error": e.detail}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, course_id):
        try:
            updated_course = update_course(course_id, request.data)
            return Response(CourseSerializer(updated_course).data, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"errors": e.detail}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, course_id):
        try:
            result = delete_course(course_id)
            return Response(result, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"errors": e.detail}, status=status.HTTP_404_NOT_FOUND)
