from rest_framework import serializers
from .models import QuizQuestion

class QuizQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizQuestion
        fields = [
            'question_id',
            'lesson_id',
            'question_text',
            'question_type',
            'options',
            'correct_answer',
            'points',
            'explanation',
            'order_number',
            'created_at',
            'updated_at'
        ]
        read_only_fields = [
            'question_id', 'created_at'
        ]
