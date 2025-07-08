from rest_framework import serializers
from .models import Forum

class ForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forum
        fields = [
            'forum_id',
            'course_id',
            'title',
            'description',
            'user_id',
            'created_date',
            'status'
        ]
        extra_kwargs = {
            'forum_id': {'read_only': True},
        }