from rest_framework import serializers
from .models import Payment_Details

class PaymentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment_Details
        fields = [
            'payment_id',
            'course_id',
            'price',
            'discount',
            'final_price',
            'promotion_id'
        ]
