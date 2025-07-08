from django.db import models
from lessons.models import Lesson

class QuizQuestion(models.Model):
    class QuestionType(models.TextChoices):
        MULTIPLE_CHOICE = 'multiple', 'multiple'
        TRUE_FALSE = 'truefalse', 'true/false'
        SHORT_ANSWER = 'short', 'short'
        ESSAY = 'essay'

    question_id = models.AutoField(primary_key=True)
    lesson_id = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='quiz_question_lesson')

    question_text = models.TextField()
    question_type = models.CharField(max_length=20, choices=QuestionType.choices)
    options = models.JSONField(blank=True, null=True)
    correct_answer = models.TextField()
    points = models.IntegerField(default=1)
    explanation = models.TextField(blank=True, null=True)
    order_number = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "QuizQuestions"

    def __str__(self):
        return f"Question {self.question_id}: {self.question_text[:50]}"