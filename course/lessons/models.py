from django.db import models
from courses.models import Course
from instructors.models import Instructor

class Lesson(models.Model):
    class ContentType(models.TextChoices):
        VIDEO = 'Video'
        TEXT = 'Text'
        QUIZ = 'Quiz'
        ASSIGNMENT = 'Assignment'
        FILE = 'File'
        LINK = 'Link'

    class Status(models.TextChoices):
        DRAFT = 'Draft'
        PUBLISHED = 'Published'

    lesson_id = models.AutoField(primary_key=True)
    coursemodule_id = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    content_type = models.CharField(max_length=20, choices=ContentType.choices)
    content = models.TextField(blank=True, null=True)
    video_url = models.CharField(max_length=255, blank=True, null=True)
    file_path = models.CharField(max_length=255, blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    is_free = models.BooleanField(default=False)
    order = models.IntegerField()
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.DRAFT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Lesson {self.title}"
