from rest_framework import serializers
from .models import LessonAttachment

class LessonAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonAttachment
        fields = [
            'attachment_id',  # Tương ứng với AttachmentID
            'lesson_id',      # Tương ứng với LessonID (ForeignKey)
            'title',
            'file_path',
            'file_type',
            'file_size',
            'download_count',
            'created_date',
        ]