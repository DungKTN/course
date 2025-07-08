from rest_framework import serializers
from .models import ForumTopic

class ForumTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumTopic
        fields = [
            'topic_id',
            'forum_id',
            'title',
            'content',
            'user_id',
            'created_date',
            'updated_date',
            'status'
        ]
        extra_kwargs = {
            'topic_id': {'read_only': True},
        }