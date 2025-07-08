from django.db import models
from payments.models import Payment
from courses.models import Course
from promotions.models import Promotion
class Payment_Details(models.Model):

    payment_id = models.ForeignKey(Payment, on_delete=models.CASCADE, related_name='payment_details')
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='payment_details')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    final_price = models.DecimalField(max_digits=10, decimal_places=2)
    promotion_id = models.ForeignKey(Promotion, on_delete=models.SET_NULL, null=True, blank=True, related_name='payment_details')
    class Meta:
        db_table = 'payment_details'
        unique_together = ('payment_id', 'course_id')

    def __str__(self):
        return f"Payment {self.payment_id} - {self.course_id} - {self.final_price}"