from rest_framework import serializers
from .models import ForumComment

class ForumCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumComment
        fields = [
            'comment_id',
            'topic_id',
            'content',
            'user_id',
            'created_date',
            'updated_date',
            'parent_comment',
            'likes',
            'status',
            'is_best_answer'
        ]
        read_only_fields = ['comment_id', 'created_date', 'updated_date', 'likes']
