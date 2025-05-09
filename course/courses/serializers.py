from rest_framework import serializers
from .models import Course
from instructors.models import Instructor
from categories.models import Category

class CourseSerializer(serializers.ModelSerializer):
    instructor_id = serializers.PrimaryKeyRelatedField(
        queryset=Instructor.objects.all(), source='instructor', write_only=True
    )  # Thêm trường instructor_id để nhận pk
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )  # Thêm trường category_id để nhận pk
    class Meta:
        model = Course
        fields = [
            'course_id',
            'title',
            'description',
            'instructor',
            'instructor_id',
            'category',
            'category_id',
            'subcategory_id',
            'thumbnail',
            'price',
            'discount_price',
            'discount_start_date',
            'discount_end_date',
            'level',
            'language',
            'duration',
            'total_lessons',
            'requirements',
            'status',
            'is_featured',
            'is_public',
            'created_at',
            'updated_at',
            'published_date',
            'rating',
            'total_reviews',
            'total_students',
            'certificate',
        ]
        read_only_fields = ['created_at', 'updated_at', 'rating', 'total_reviews', 'total_students']
