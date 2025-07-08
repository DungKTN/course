from rest_framework import serializers
from .models import Support
class SupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Support
        fields = [
            'support_id',
            'user_id',
            'name',
            'email',
            'subject',
            'message',
            'status',
            'priority',
            'created_date',
            'updated_date',
            'admin_id'
        ]
        read_only_fields = [
            'support_id',
        ]