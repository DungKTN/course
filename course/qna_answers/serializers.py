from rest_framework import serializers
from .models import QnAAnswer

class QnAAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QnAAnswer
        fields = [
            'answer_id',
            'qna_id',
            'answer',
            'user_id',
            'answered_date',
            'updated_date',
            'is_accepted',
            'likes'
        ]
        extra_kwargs = {
            'answer_id': {'read_only': True},
        }