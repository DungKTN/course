from rest_framework import serializers
from .models import Promotion

class PromotionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Promotion
        fields = [
            'promotion_id',
            'code',
            'description',
            'discount_type',
            'discount_value',
            'start_date',
            'end_date',
            'usage_limit',
            'used_count',
            'min_purchase',
            'max_discount',
            'applicable_courses',
            'applicable_categories',
            'admin_id',  
            'status',
            'created_date',
            'updated_date'
        ]
        read_only_fields = [
            'promotion_id', 'created_date'
        ]