from django.db import models
from users.models import User
from courses.models import Course
from promotions.models import Promotion

class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_user')
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='cart_course')
    promotion_id = models.ForeignKey(
        Promotion,
        on_delete=models.CASCADE,
        related_name='cart_promotion',
        null=True, blank=True  # Cho phép null và không bắt buộc
    )
    added_date = models.DateTimeField()

    class Meta:
        db_table = 'Cart'
        constraints = [
            models.UniqueConstraint(fields=['user_id', 'course_id'], name='unique_cart')
        ]

    def __str__(self):
        return f"Cart {self.cart_id}: User {self.user_id}, Course {self.course_id}"
