from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            'course_id',
            'title',
            'description',
            'instructor_id',
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
