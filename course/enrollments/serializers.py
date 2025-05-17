from rest_framework import serializers
from .models import Enrollment

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = [
            'enrollment_id',
            'user_id',
            'course_id',
            'enrollment_date',
            'status',
            'progress',
            'certificate_issue_date'
        ]
        read_only_fields = [
            'enrollment_id', 'enrollment_date'
        ]
class EnrollmentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = [
            'user_id',
            'course_id',
            'enrollment_date',
            'status',
            'progress',
            'certificate_issue_date'
        ]
        read_only_fields = [
            'enrollment_id', 'enrollment_date'
        ]