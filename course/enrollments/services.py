from rest_framework.exceptions import ValidationError
from serializers import EnrollmentSerializer, EnrollmentCreateSerializer
from .models import Enrollment
from datetime import datetime
from courses.models import Course
def create_enrollment(user_id, course_id):
    try: 
        data = {
            'user_id': user_id,
            'course_id': course_id,
            'enrollment_date': datetime.now(),   
            'status': Enrollment.Status.Active,
            'progress': 0,
            'certificate_issued': 'null',
        }
        serializer = EnrollmentCreateSerializer(data)
        if serializer.is_valid(raise_exception=True):
            enrollment = serializer.save()
            course = Course.objects.get(course_id=course_id)
            course.total_students += 1
            course.save()
            return enrollment
        raise ValidationError(serializer.errors)
    except Exception as e:
        raise ValidationError({"error": str(e)})
def get_enrollment_by_user(user_id):
    try:
        enrollment = Enrollment.objects.get(user_id=user_id)
        serializer = EnrollmentSerializer(enrollment)
        return serializer.data
    except Enrollment.DoesNotExist:
        raise ValidationError({"error": "Enrollment not found."})
    except Exception as e:
        raise ValidationError({"error": str(e)})
def find_enrollment_by_id(enrollment_id):
    try:
        enrollment = Enrollment.objects.get(enrollment_id=enrollment_id)
        serializer = EnrollmentSerializer(enrollment)
        return serializer.data
    except Enrollment.DoesNotExist:
        raise ValidationError({"error": "Enrollment not found."})
    except Exception as e:
        raise ValidationError({"error": str(e)})
def find_by_user_and_course(user_id, course_id):
    try:
        enrollment = Enrollment.objects.get(user_id=user_id, course_id=course_id)
        serializer = EnrollmentSerializer(enrollment)
        return serializer.data
    except Enrollment.DoesNotExist:
        raise ValidationError({"error": "Enrollment not found."})
    except Exception as e:
        raise ValidationError({"error": str(e)})
def count_enrollments_by_course(course_id):
    try:
        count = Enrollment.objects.filter(course_id=course_id).count()
        return count
    except Exception as e:
        raise ValidationError({"error": str(e)})
def has_access(user_id, course_id):
    try:
        enrollment = Enrollment.objects.get(user_id=user_id, course_id=course_id)
        if enrollment.status == Enrollment.Status.Active:
            return True
        return False
    except Enrollment.DoesNotExist:
        raise ValidationError({"error": "Enrollment not found."})
    except Exception as e:
        raise ValidationError({"error": str(e)})
def process_enrollment(enrollment_id):
    try:
        enrollment = Enrollment.objects.get(enrollment_id=enrollment_id)
        if enrollment.progress == 100:
            enrollment.status = Enrollment.Status.Complete
            enrollment.completion_date = datetime.now()
            enrollment.certificate = "Certificate of Completion"
            enrollment.certificate_issue_date = datetime.now()
            enrollment.save()
        else:
            enrollment.progress += 
        return {"message": "Enrollment completed successfully."}
    except Enrollment.DoesNotExist:
        raise ValidationError({"error": "Enrollment not found."})
    except Exception as e:
        raise ValidationError({"error": str(e)})
