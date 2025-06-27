from django.db import models
from lessons.models import Lesson

class LessonAttachment(models.Model):
    attachment_id = models.AutoField(primary_key=True)
    lesson_id = models.ForeignKey(Lesson,on_delete=models.CASCADE,related_name='attachments')
    title = models.CharField(max_length=255, null=True, blank=True)
    file_path = models.CharField(max_length=255)
    file_type = models.CharField(max_length=50, null=True, blank=True)
    file_size = models.IntegerField(null=True, blank=True)
    download_count = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'LessonAttachments'

    def __str__(self):
        return self.title or f'Attachment {self.attachment_id}'
