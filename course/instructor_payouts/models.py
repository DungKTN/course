from django.db import models
from instructors.models import Instructor
from admins.models import Admin

class InstructorPayout(models.Model):
    class PayoutStatusChoices(models.TextChoices):
        PENDING = 'pending', 'pending'
        PROCESSED = 'processed', 'processed'
        CANCELLED = 'cancelled', 'cancelled'
        FAILED = 'failed', 'failed'

    payout_id = models.AutoField(primary_key=True)
    instructor_id = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='payouts')
    amount = models.DecimalField(max_digits=15, decimal_places=2)         # Tổng số tiền
    fee = models.DecimalField(max_digits=15, decimal_places=2, default=0) # Phí nền tảng (nếu có)
    net_amount = models.DecimalField(max_digits=15, decimal_places=2)     # Tiền thực nhận
    payment_method = models.CharField(max_length=100)                     # Ví dụ: Bank Transfer
    transaction_id = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=20, choices=PayoutStatusChoices.choices, default=PayoutStatusChoices.PENDING)
    request_date = models.DateTimeField(auto_now_add=True)
    processed_date = models.DateTimeField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    period = models.CharField(max_length=20)  # Ví dụ: "2025-07" để thống kê tháng
    processed_by = models.ForeignKey(Admin, on_delete=models.SET_NULL, null=True, blank=True, related_name='processed_payouts')

    class Meta:
        db_table = 'InstructorPayouts'
        ordering = ['-request_date']

    def __str__(self):
        return f"Payout #{self.payout_id} - {self.instructor_id.user_id.full_name} - {self.status}"
