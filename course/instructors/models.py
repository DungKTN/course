from django.db import models
from users.models import User


class Instructor(models.Model):
    instructor_id = models.AutoField(primary_key=True)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)

    bio = models.TextField(null=True, blank=True)
    specialization = models.CharField(max_length=255, null=True, blank=True)
    qualification = models.CharField(max_length=255, null=True, blank=True)
    experience = models.IntegerField(null=True, blank=True)

    social_links = models.JSONField(null=True, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)

    total_students = models.IntegerField(default=0)
    total_courses = models.IntegerField(default=0)

    payment_info = models.JSONField(null=True, blank=True)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Instructors'

    def __str__(self):
        return f"Instructor {self.instructor_id} - {self.user.full_name}"
