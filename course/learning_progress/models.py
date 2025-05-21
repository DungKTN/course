from django.db import models
from enrollments.models import Enrollment
from lessons.models import Lesson

class LearningProgress(models.Model):
    class StatusChoices(models.TextChoices):
        IN_PROGRESS = 'progress', 'progress'
        COMPLETED = 'completed', 'completed'
        PENDING = 'pending', 'pending'

    progress_id = models.AutoField(primary_key=True)
    enrollment_id = models.ForeignKey(Enrollment, on_delete=models.CASCADE, related_name='learning_progress')
    lesson_id = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='learning_progress')
    progress = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    last_accessed = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.PENDING
    )
    start_time = models.DateTimeField(blank=True, null=True)
    completion_time = models.DateTimeField(blank=True, null=True)
    time_spent = models.IntegerField(null=True, blank=True)
    last_position = models.IntegerField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    class Meta:
        db_table = 'LearningProgress'
        constraints = [
            models.UniqueConstraint(fields=['enrollment', 'lesson'], name='unique_learning_progress')
        ]