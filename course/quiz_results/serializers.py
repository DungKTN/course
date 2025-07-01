from rest_framework import serializers
from .models import QuizResult

class QuizResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizResult
        fields = [
            'quiz_result_id',
            'Enrollment_id',
            'Lesson_id',
            'start_time',
            'submit_time',
            'time_taken',
            'total_questions',
            'corret_answers',
            'total_points',
            'score',
            'answers',
            'passed',
            'attempt'
        ]
        read_only_fields = [
            'quiz_result_id'
        ] 