from rest_framework.exceptions import ValidationError
from .serializers import PaymentSerializer
from .models import Payment
from datetime import datetime
from courses.models import Course
from django.db import IntegrityError


def create_payment(data):
    try:
        
        serializer = PaymentSerializer(data={
            "user_id": data.get("user_id"),
            "course_id": data.get("course_id"),
            "amount": data.get("amount"),
            "discount_amount": data.get("discount_amount", 0),
            "total_amount": data.get("total_amount"),
            "transaction_id": data.get("transaction_id"),
            "payment_date": datetime.now(),
            "payment_status": Payment.PaymentStatus.PENDING,
            "payment_method": data.get("payment_method", Payment.PaymentMethod.VNPAY),
            "refund_amount": 0,
            "refund_reason": None,
            "refund_date": None,
            "payment_gateway": data.get("payment_gateway"),
            "gateway_response": data.get("gateway_response")
        })
        if serializer.is_valid():
            payment = serializer.save()
            return payment
        else:
            raise ValidationError(serializer.errors)
    except IntegrityError as e:
        raise ValidationError({"error": str(e)})
    except Exception as e:
        raise ValidationError({"error": str(e)})