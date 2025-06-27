from rest_framework import serializers
from .models import Cart

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = [
            'cart_id',
            'user_id',
            'course_id',
            'promotion_id',
            'added_date'
        ]
        read_only_fields = [
            'cart_id'
        ]