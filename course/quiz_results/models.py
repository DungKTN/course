from django.db import models
from enrollments.models import Enrollment
from lessons.models import Lesson

class QuizResult(models.Model):
    quiz_result_id = models.AutoField(primary_key=True)
    Enrollment_id = models.ForeignKey(Enrollment, on_delete=models.CASCADE, related_name='quiz_result_enrollment')
    Lesson_id = models.ForeignKey(Lesson, on_delete= models.CASCADE, related_name='quiz_result_lesson')
    start_time = models.DateTimeField(null=True, blank=True)
    submit_time = models.DateTimeField(null=True, blank=True)
    time_taken = models.IntegerField(null=True, blank=True)
    total_questions = models.IntegerField(null=True, blank=True)
    corret_answers = models.IntegerField(null=True, blank=True)
    total_points = models.IntegerField(null=True, blank=True)
    score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    answers = models.JSONField(null=True, blank=True)
    passed = models.BooleanField(default=False)
    attempt = models.IntegerField(default=1)

    class Meta:
        db_table = 'QuizResult'
        constraints = [
            models.UniqueConstraint(fields=['Enrollment_id', 'Lesson_id'], name='unique_quiz_result')
        ]

    def __str__(self):
        return f"QuizResult {self.quiz_result_id}: Enrollment {self.Enrollment_id}, Lesson {self.Lesson_id}"