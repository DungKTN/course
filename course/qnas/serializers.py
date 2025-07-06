from rest_framework import serializers
from .models import QnA

class QnASerializer(serializers.ModelSerializer):
    class Meta:
        model = QnA
        fields = [
            'qna_id',
            'course_id',
            'lesson_id',
            'question',
            'user_id',
            'asked_date',
            'status',
            'views'
        ]
        extra_kwargs = {
            'qna_id': {'read_only': True},
        }