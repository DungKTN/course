from .models import Course
from django.utils import timezone
from django.shortcuts import get_object_or_404

def create_course(data):
    """Tạo một khóa học mới"""
    course = Course.objects.create(**data)
    return course

def update_course(course_id, data):
    """Cập nhật thông tin khóa học"""
    course = get_object_or_404(Course, pk=course_id)
    for field, value in data.items():
        setattr(course, field, value)
    course.updated_at = timezone.now()
    course.save()
    return course

def delete_course(course_id):
    """Xóa khóa học"""
    course = get_object_or_404(Course, pk=course_id)
    course.delete()
    return True

def get_course(course_id):
    """Lấy chi tiết một khóa học"""
    return get_object_or_404(Course, pk=course_id)

def list_courses(filters=None):
    """Danh sách các khóa học, có thể lọc"""
    queryset = Course.objects.all()
    if filters:
        queryset = queryset.filter(**filters)
    return queryset
