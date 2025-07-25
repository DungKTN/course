from django.db import models
from users.models import User
from courses.models import Course
import uuid
from promotions.models import Promotion
class Payment(models.Model):
    class PaymentStatus(models.TextChoices):
        PENDING = 'pending', 'pending'
        COMPLETED = 'completed', 'completed'
        FAILED = 'failed', 'failed'
        REFUNDED = 'refunded', 'refunded'
        CANCELLED = 'cancelled', 'cancelled'
    class PaymentMethod(models.TextChoices):
        VNPAY = 'vnpay', 'vnpay'
        MOMO = 'momo', 'momo'
    payment_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payment_user_id')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    transaction_id = models.CharField(max_length=255, unique=True, null=True, blank=True)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=20,
        choices=PaymentStatus.choices,
        default=PaymentStatus.PENDING
    )
    payment_method = models.CharField(
        max_length=20,
        choices=PaymentMethod.choices,
        default=PaymentMethod.VNPAY 
    )
    promotion_id = models.ForeignKey(
        Promotion, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='payments_discount'
    )
    refund_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    payment_gateway = models.CharField(max_length=255)
    gateway_response = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "payments"

    def __str__(self):
        return f"Payment {self.transaction_id} - {self.payment_status} - {self.payment_id} - {self.payment_date} DATE"
