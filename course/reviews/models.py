from django.db import models
from courses.models import Course
from users.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = 'pending', 'pending'
        APPROVED = 'approved', 'approved'
        REJECTED = 'rejected', 'rejected'

    review_id = models.AutoField(primary_key=True)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE,related_name='reviews_course')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,related_name='reviews_user')

    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    comment = models.TextField(blank=True, null=True)
    review_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=StatusChoices, default=StatusChoices.PENDING)
    likes = models.PositiveIntegerField(default=0)
    report_count = models.PositiveIntegerField(default=0)
    instructor_response = models.TextField(blank=True, null=True)
    response_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-review_date'] # Mới nhất lên đầu
        ordering = ['-likes'] # Đánh giá nhiều nhất lên đầu

    def __str__(self):
        return f'Review by {self.user_id} for {self.course_id}'