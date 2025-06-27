from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            'review_id',
            'course_id',
            'user_id',
            'rating',
            'comment',
            'review_date',
            'updated_date',
            'status',
            'likes',
            'report_count',
            'instructor_response',
            'response_date',
        ]
        read_only_fields = ['review_id', 'review_date', 'updated_date', 'likes', 'report_count', 'response_date']