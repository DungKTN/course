from rest_framework import serializers
from .models import Lesson

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = [
            'lesson_id',
            'coursemodule_id',
            'title',
            'description',
            'content_type',
            'content',
            'video_url',
            'file_path',
            'duration',
            'is_free',
            'order',
            'status',
            'created_at',
            'updated_at',

        ]
