from django.db import models
from users.models import User
from courses.models import Course
from promotions.models import Promotion

class Wishlist(models.Model):
    wishlist_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wishlist_user')
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='wishlist_course')
    added_date = models.DateTimeField()

    class Meta:
        db_table = 'Wishlist'
        constraints = [
            models.UniqueConstraint(fields=['user_id', 'course_id'], name='unique_wishlist')
        ]

    def __str__(self):
        return f"Wishlist {self.wishlist_id}: User {self.user_id}, Course {self.course_id}"
