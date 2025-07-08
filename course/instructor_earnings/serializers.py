from rest_framework import serializers
from .models import InstructorEarning

class InstructorEarningSerializer(serializers.ModelSerializer):
    instructor_name = serializers.CharField(source='instructor.user_id.full_name', read_only=True)
    course_title = serializers.CharField(source='course.title', read_only=True)
    payment_transaction_id = serializers.CharField(source='payment.transaction_id', read_only=True)

    class Meta:
        model = InstructorEarning
        fields = [
            'earning_id',
            'instructor_id',
            'instructor_name',
            'course_id',
            'course_title',
            'payment_id',
            'payment_transaction_id',
            'amount',
            'net_amount',
            'status',
            'earning_date',
            'instructor_payout_id',
        ]
        read_only_fields = ['earning_id', 'earning_date', 'net_amount']
