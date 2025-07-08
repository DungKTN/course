from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .services import (
    create_course,
    update_course,
    delete_course,
    get_all_courses,
    get_course_by_id
)

class CourseListView(APIView):
    def get(self, request):
        try:
            courses = get_all_courses()
            return Response(courses, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"errors": str(e)}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        try:
            course = create_course(request.data)
            return Response(course, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({"errors": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, course_id):
        try:
            course = update_course(course_id, request.data)
            return Response(course, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"errors": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, course_id):
        try:
            result = delete_course(course_id)
            return Response(result, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"errors": str(e)}, status=status.HTTP_404_NOT_FOUND)
        
class CourseDetailView(APIView):
    def get(self, request, course_id):
        try:
            course = get_course_by_id(course_id)
            return Response(course, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"errors": str(e)}, status=status.HTTP_404_NOT_FOUND)