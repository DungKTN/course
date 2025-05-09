from rest_framework import serializers
from .models import Course
from instructors.models import Instructor
from instructors.serializers import InstructorSerializers  # giả sử đã có sẵn

class CourseSerializer(serializers.ModelSerializer):
    instructor = InstructorSerializers(read_only=True)  # hiển thị nested object khi đọc
    instructor_id = serializers.PrimaryKeyRelatedField(
        queryset=Instructor.objects.all(), source='instructor', write_only=True
    )  # cho phép gửi instructor_id khi ghi

    class Meta:
        model = Course
        fields = [
            'course_id',
            'title',
            'description',
            'instructor',        # hiển thị nested khi đọc
            'instructor_id',     # ghi bằng id
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
        read_only_fields = [
            'created_at', 'updated_at', 'rating', 'total_reviews', 'total_students'
        ]
