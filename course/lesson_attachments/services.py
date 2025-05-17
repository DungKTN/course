from rest_framework.exceptions import ValidationError
from .models import LessonAttachment
from .serializers import LessonAttachmentSerializer
from .models import LessonAttachment

def validate_lesson_attachment_data(data):
    serializer = LessonAttachmentSerializer(data=data)
    if serializer.is_valid():
        return {"message": "Data is valid."}
    return {"errors": serializer.errors}

def get_lesson_attachments():
    lesson_attachments = LessonAttachment.objects.all()
    if not lesson_attachments.exists():
        raise ValidationError({"error": "No lesson attachments found."})
    return lesson_attachments  # Trả về queryset trực tiếp

def get_lesson_attachment_by_id(attachment_id):
    try:
        lesson_attachment = LessonAttachment.objects.get(attachment_id=attachment_id)
        serializer = LessonAttachmentSerializer(lesson_attachment)
        return serializer.data
    except LessonAttachment.DoesNotExist:
        raise ValidationError({"error": "Lesson attachment not found."})

def create_lesson_attachment(data):
    """Tạo một attachment bài học mới."""
    serializer = LessonAttachmentSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        lesson_attachment = serializer.save()
        return lesson_attachment
    raise ValidationError(serializer.errors)

def update_lesson_attachment(attachment_id, data):
    try:
        lesson_attachment = LessonAttachment.objects.get(attachment_id=attachment_id)
    except LessonAttachment.DoesNotExist:
        raise ValidationError({"error": "Lesson attachment not found."})

    serializer = LessonAttachmentSerializer(lesson_attachment, data=data, partial=True)
    if serializer.is_valid(raise_exception=True):
        updated_lesson_attachment = serializer.save()
        return updated_lesson_attachment
    raise ValidationError(serializer.errors)

def delete_lesson_attachment(attachment_id):
    try:
        lesson_attachment = LessonAttachment.objects.get(attachment_id=attachment_id)
        lesson_attachment.delete()
        return {"message": "Lesson attachment deleted successfully."}
    except LessonAttachment.DoesNotExist:
        raise ValidationError({"error": "Lesson attachment not found."})