from rest_framework import serializers
from .models import CourseModule

class CourseModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseModule
        fields = [
            'id',           # Tương ứng với ModuleID
            'course_id',       # Tương ứng với CourseID (ForeignKey)
            'title',
            'description',
            'order_number',
            'duration',
            'status',
            'created_date',
            'updated_date',
        ]