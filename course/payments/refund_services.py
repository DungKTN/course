from payments.models import Payment
from payment_details.models import Payment_Details
from enrollments.models import Enrollment
from django.db import transaction
from datetime import datetime
from django.utils import timezone
from rest_framework.exceptions import ValidationError
from decimal import Decimal
refund_conditions = 50
def refund_request(payment_id, payment_details_ids , reason=None):
    try:
        with transaction.atomic():
            try:
                payment = Payment.objects.prefetch_related('payment_details').get(payment_id=payment_id)
            except Payment.DoesNotExist:
                raise ValidationError("Payment not found.")
            if payment.payment_status != Payment.PaymentStatus.COMPLETED:
                raise ValidationError("Only completed payments can be refunded.")
            if payment.refund_amount >= payment.total_amount:
                raise ValidationError("Refund amount exceeds total payment amount.")
            
            if not payment_details_ids:
                raise ValidationError("Payment details IDs are required for refund processing.")
            if payment.payment_details:
                valid_ids = set(payment.payment_details.all().values_list('id', flat=True))
                if not set(payment_details_ids).issubset(valid_ids):
                    raise ValidationError("Some payment details IDs do not belong to the specified payment.")
                refund_items = payment.payment_details.filter(id__in=payment_details_ids)

                enrollments = Enrollment.objects.filter(payment_id=payment_id, course_id__in=refund_items.values_list('course_id', flat=True))
                if not enrollments.exists():
                    raise ValidationError("No enrollments found for the given payment IDs.")
                for enrollment in enrollments:
                    if enrollment.status != Enrollment.Status.Active:
                        raise ValidationError("Only active enrollments can be refunded.")
                    if enrollment.progress > refund_conditions:
                        raise ValidationError("Refund is not allowed if more than 50% of the course has been completed.")
                    if enrollment.expiry_date and enrollment.expiry_date < timezone.now():
                        raise ValidationError("Refund is not allowed for expired courses.")
                for detail in refund_items:
                    detail.refund_status = Payment_Details.RefundStatus.PENDING
                    detail.refund_request_time = timezone.now()
                    detail.refund_reason = reason
                    detail.refund_amount =Decimal(( detail.final_price/ payment.amount) * payment.total_amount, 2)
                    detail.save()
                        
    except  Exception as e:
        raise ValidationError(f"Error processing refund: {str(e)}")     