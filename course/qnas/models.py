from django.db import models
from courses.models import Course
from lessons.models import Lesson
from enrollments.models import Enrollment
from users.models import User

class QnA(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = 'Pending', 'Pending'
        ANSWERED = 'Answered', 'Answered'
        CLOSED = 'Closed', 'Closed'

    qna_id = models.AutoField(primary_key=True)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='qna_course')
    lesson_id = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='qna_lesson')
    question = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='qna_user', db_column='user_id')
    asked_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=StatusChoices.choices, default=StatusChoices.PENDING)
    views = models.IntegerField(default=0)

    class Meta:
        db_table = 'QnA'


    def __str__(self):
        return f"QnA #{self.qna_id}: Student {self.user_id}"
