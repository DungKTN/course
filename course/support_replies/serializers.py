from rest_framework import serializers
from .models import SupportReply
class SupportReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportReply
        fields = ['reply_id', 'support_id', 'user_id', 'admin_id', 'message', 'created_at']
        read_only_fields = ['reply_id', 'created_at']  # id and created_at should not be editable by users