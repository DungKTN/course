from rest_framework import serializers
from .models import LearningProgress

class LearningProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningProgress
        fields = [
            'progress_id',
            'enrollment_id',
            'lesson_id',
            'progress',
            'last_accessed',
            'status',
            'start_time',
            'completion_time',
            'time_spent',
            'last_position',
            'notes'
        ]
        read_only_fields = ['progress_id', 'last_accessed']
        extra_kwargs = {
            'enrollment_id': {'required': True},
            'lesson_id': {'required': True},
            'progress': {'required': True},
            'status': {'required': True},
            'start_time': {'required': False},
            'completion_time': {'required': False},
            'time_spent': {'required': False},
            'last_position': {'required': False},
            'notes': {'required': False}
        }