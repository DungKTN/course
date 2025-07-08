from rest_framework.exceptions import ValidationError
from .serializers import InstructorPayoutSerializer
from .models import InstructorPayout
from django.db import transaction
from django.utils import timezone
from instructor_earnings.models import InstructorEarning
from admins.models import Admin
from django.db.models import Sum
from decimal import Decimal

def admin_create_instructor_payout(instructor_id,  processed_by, transaction_id=None, notes='', period=None):
    try:
        if not instructor_id:
            raise ValidationError("Instructor ID is required.")

        earnings = InstructorEarning.objects.filter(
            instructor_id=instructor_id,
            status=InstructorEarning.StatusChoices.AVAILABLE,
            instructor_payout_id__isnull=True  # tránh duplicate payout
        )

        if not earnings.exists():
            raise ValidationError("No available earnings for this instructor.")

        total_amount = earnings.aggregate(total=Sum('net_amount'))['total'] or Decimal('0.00')

        payout = InstructorPayout.objects.create(
            instructor_id=instructor_id,
            amount=total_amount,
            period=period or timezone.now().strftime("%Y-%m"),
            processed_by=processed_by,
            transaction_id=transaction_id,
            notes=notes,
            status=InstructorPayout.PayoutStatusChoices.PENDING,
            request_date=timezone.now(),
        )

        
        earnings.update(instructor_payout_id=payout)

        return InstructorPayoutSerializer(payout).data

    except Exception as e:
        raise ValidationError(f"Error creating payout: {str(e)}")

