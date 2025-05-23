from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = [
            'payment_id',
            'user_id',
            'course_id',
            'amount',
            'discount_amount',
            'total_amount',
            'transaction_id',
            'payment_date',
            'payment_status',
            'payment_method',
            'refund_amount',
            'refund_reason',
            'refund_date',
            'payment_gateway',
            'gateway_response'
        ]
