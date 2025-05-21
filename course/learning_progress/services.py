from rest_framework.exceptions import ValidationError
from django.utils import timezone
from .models import LearningProgress
from .serializers import LearningProgressSerializer
from enrollments.models import Enrollment
from lessons.models import Lesson
def update_learning_progress(enrollment_id, lesson_id, progress_data):
    try:
        enrollment = Enrollment.objects.get(enrollment_id=enrollment_id)
        lesson = Lesson.objects.get(lesson_id=lesson_id)

        learning_progress, created = LearningProgress.objects.get_or_create(
            enrollment_id=enrollment,
            lesson_id=lesson,
            defaults={
                'progress': progress_data['progress'],
                'status': progress_data['status'],
                'start_time': timezone.now(),
                'last_accessed': timezone.now()
            }
        )

        if not created:
            # Update existing LearningProgress entry
            learning_progress.progress = progress_data['progress']
            learning_progress.status = progress_data['status']
            learning_progress.last_accessed = timezone.now()
            learning_progress.save()

        return LearningProgressSerializer(learning_progress).data
    except Enrollment.DoesNotExist:
        raise ValidationError("Enrollment not found.")
    except Lesson.DoesNotExist:
        raise ValidationError("Lesson not found.")
    except Exception as e:
        raise ValidationError(f"An error occurred: {str(e)}")
def get_learning_progress(data):
    try:
        learning_progress = LearningProgress.objects.get(
            enrollment_id=data.enrollment_id,
            lesson_id=data.lesson_id
        )
        return LearningProgressSerializer(learning_progress).data
    except LearningProgress.DoesNotExist:
        raise ValidationError("Learning progress not found.")
    except Exception as e:
        raise ValidationError(f"An error occurred: {str(e)}")
def get_all_learning_progress_by_enrollment(enrollment_id):
    try:
        learning_progress = LearningProgress.objects.filter(enrollment_id=enrollment_id)
        return LearningProgressSerializer(learning_progress, many=True).data
    except Exception as e:
        raise ValidationError(f"An error occurred: {str(e)}")
def delete_learning_progress(enrollment_id, lesson_id):
    try:
        learning_progress = LearningProgress.objects.get(
            enrollment_id=enrollment_id,
            lesson_id=lesson_id
        )
        learning_progress.delete()
        return {"message": "Learning progress deleted successfully."}
    except LearningProgress.DoesNotExist:
        raise ValidationError("Learning progress not found.")
    except Exception as e:
        raise ValidationError(f"An error occurred: {str(e)}")

