from .models import Admin
from rest_framework import serializers

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = [
            'admin_id',
            'user_id',
            'department',
            'role',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['admin_id', 'created_at', 'updated_at']