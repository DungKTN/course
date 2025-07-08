from django.db import models
from instructors.models import Instructor
from courses.models import Course
from payments.models import Payment
from instructor_payouts.models import InstructorPayout  # Assuming you have a separate payouts model for instructor payouts

class InstructorEarning(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = 'pending', 'pending'              
        AVAILABLE = 'available', 'available'       
        PAID = 'paid', 'paid'                      
        CANCELLED = 'cancelled', 'cancelled'     

    earning_id = models.AutoField(primary_key=True)
    instructor_id = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='earnings')
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='earnings')
    payment_id = models.ForeignKey(Payment, on_delete=models.CASCADE, related_name='instructor_earnings')

    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Tổng tiền khóa học (sau giảm giá)
    net_amount = models.DecimalField(max_digits=10, decimal_places=2)  # = amount * (100 - commission_rate) / 100

    status = models.CharField(
        max_length=10,
        choices=StatusChoices.choices,
        default=StatusChoices.PENDING
    )

    earning_date = models.DateTimeField(auto_now_add=True)
    instructor_payout_id = models.ForeignKey(
        InstructorPayout, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='earnings'
    )

    class Meta:
        db_table = 'InstructorEarnings'
        verbose_name = 'Instructor Earning'
        verbose_name_plural = 'Instructor Earnings'
        indexes = [
            models.Index(fields=['status']),
            models.Index(fields=['instructor_id']),
            models.Index(fields=['course_id']),
        ]
        unique_together = [
            ('payment_id', 'course_id', 'instructor_id')]

    def __str__(self):
        return f"[{self.earning_id}] {self.instructor_id.user_id.full_name} - {self.course_id.title} - {self.net_amount} VND"
