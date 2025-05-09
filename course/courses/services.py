from rest_framework.exceptions import ValidationError
from .models import Course
from .serializers import CourseSerializer

def create_course(data):
    try:
        instructor_instance = data.pop('instructor')  # Lấy instructor từ data
        category_instance = data.pop('category')  # Lấy category từ data
    except KeyError:
        raise ValidationError({"instructor": "Missing required fields."})
    serializer = CourseSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        course = serializer.save()
        return course
    raise ValidationError(serializer.errors)

def update_course(course_id, data):
    try:
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        raise ValidationError({"error": "Course not found."})

    serializer = CourseSerializer(course, data=data, partial=True)
    if serializer.is_valid(raise_exception=True):
        updated_course = serializer.save()
        return updated_course
    raise ValidationError(serializer.errors)

def delete_course(course_id):
    try:
        course = Course.objects.get(course_id=course_id)
        course.delete()
        return {"message": "Course deleted successfully."}
    except Course.DoesNotExist:
        raise ValidationError({"error": "Course not found."})

def get_course_by_id(course_id):
    try:
        course = Course.objects.get(id=course_id)
        serializer = CourseSerializer(course)
        return serializer.data
    except Course.DoesNotExist:
        raise ValidationError({"error": "Course not found."})

def get_all_courses():
    courses = Course.objects.all()
    if not courses.exists():
        raise ValidationError({"error": "No courses found."})
    serializer = CourseSerializer(courses, many=True)
    return serializer.data

def validate_course_data(data):
    serializer = CourseSerializer(data=data)
    if serializer.is_valid():
        return {"message": "Data is valid."}
    return {"errors": serializer.errors}
