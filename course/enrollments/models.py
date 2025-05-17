from django.db import models
from users.models import User
from courses.models import Course

class Enrollment(models.Model):
    class Status(models.TextChoices):
        Active = "active"
        Complete = "complete"
        Expired = "exoired"
        Cancelled = "cancelled"
    enrollment_id = models.AutoField(primary_key=True)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    course_id = models.OneToOneField(Course)
    enrollment_date = models.DateTimeField(blank=True, null=True)
    expiry_date = models.DateTimeField(blank=True, null = True)
    completion_date = models.DateTimeField(blank=True, null = True)
    progress = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.Active
    )
    certificate = models.CharField(max_length=255, blank=True, null=True)
    certificate_issue_date = models.DateTimeField(null=True, blank=True)
    last_access_date = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = 'Enrollments'
        
def __str__(self):
    return f"Enrollment {self.status} - {self.certificate}"



