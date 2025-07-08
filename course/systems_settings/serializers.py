from rest_framework import serializers
from .models import SystemsSetting

class SystemsSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemsSetting
        fields = [
            'setting_id',
            'setting_group',
            'setting_key',
            'setting_value',
            'description',
            'admin_id',
            'updated_date'
        ]
        read_only_fields = ['setting_id']
