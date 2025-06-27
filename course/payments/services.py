from django.db import transaction
from rest_framework.exceptions import ValidationError
from .serializers import PaymentSerializer, PaymentCreateSerializer
from .models import Payment
from promotions.models import Promotion
from payment_details.serializers import PaymentDetailSerializer
from .utils import generate_unique_transaction_id

def create_payment(payment_data):
    try:
        with transaction.atomic():
            # 1. Validate payment
            payment_serializer = PaymentCreateSerializer(data={
                'user_id': payment_data.get('user_id'),
                'amount': payment_data.get('amount'),
                'promotion_id': payment_data.get('promotion_id'),
                'discount_amount': payment_data.get('discount_amount', 0),
                'total_amount': payment_data.get('total_amount'),
                'payment_method': payment_data.get('payment_method'),
                'transaction_id': generate_unique_transaction_id(),
            })

            if not payment_serializer.is_valid():
                raise ValidationError({"payment": payment_serializer.errors})

            promotion_id = payment_serializer.validated_data.get('promotion_id')
            if promotion_id and not Promotion.objects.filter(promotion_id=promotion_id).exists():
                print("⚠️ Promotion không tồn tại – tiếp tục không áp dụng khuyến mãi.")
            payment = payment_serializer.save()
            print("✅ Payment created successfully: %s", payment.payment_id)
            payment_detail_data = payment_data.get('payment_details')
            if not payment_detail_data:
                raise ValidationError("Thiếu thông tin chi tiết thanh toán (payment_details)")
            payment_detail_arr = [
                {
                    'payment_id': payment.payment_id,
                    'course_id': detail.get('course_id'),
                    'price': detail.get('price'),
                    'discount': detail.get('discount', 0),
                    'final_price': detail.get('final_price'),
                    'primotion_id': detail.get('promotion_id')
                }
                for detail in payment_detail_data
            ]
            payment_detail_serializer = PaymentDetailSerializer(data=payment_detail_arr, many=True)

            if not payment_detail_serializer.is_valid():
                raise ValidationError({"payment_details": payment_detail_serializer.errors})

            # 5. Lưu payment_detail
            payment_detail_serializer.save()

            return {
                "payment": PaymentSerializer(payment).data,
                "payment_details": payment_detail_serializer.data
            }

    except Exception as e:
        raise ValidationError(f"Error creating payment: {str(e)}")
