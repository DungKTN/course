from rest_framework.exceptions import ValidationError
from .models import Instructor
from .serializers import InstructorSerializers
from  users.models import User

def create_instructor(data):
    """Tạo một giảng viên mới."""
    try:
        user_instance = User.objects.get(pk=data['user_id'])  # Truy cập qua data
    except User.DoesNotExist:
        raise ValidationError({"user_id": "User with this ID does not exist."})
    # Sửa đổi data để truyền user instance, không phải user_id
    modified_data = data.copy()  # Tạo bản sao để không ảnh hưởng đến dữ liệu gốc
    modified_data['user'] = user_instance
    serializer = InstructorSerializers(data=modified_data, context={'request': None})  # Truyền modified_data
    if serializer.is_valid(raise_exception=True):
        instructor = serializer.save()
        return instructor
    raise ValidationError(serializer.errors)


def update_instructor(instructor_id, data):
    try:
        instructor = Instructor.objects.get(instructor_id=instructor_id)
    except Instructor.DoesNotExist:
        raise ValidationError({"error": "Instructor not found."})

    serializer = InstructorSerializers(instructor, data=data, partial=True)
    if serializer.is_valid(raise_exception=True):
        updated_instructor = serializer.save()
        return updated_instructor
    raise ValidationError(serializer.errors)

def delete_instructor(instructor_id):
    try:
        instructor = Instructor.objects.get(instructor_id=instructor_id)
        instructor.delete()
        return {"message": "Instructor deleted successfully."}
    except Instructor.DoesNotExist:
        raise ValidationError({"error": "Instructor not found."})

def validate_instructor_data(data):
    serializer = InstructorSerializers(data=data)
    if serializer.is_valid():
        return {"message": "Data is valid."}
    return {"errors": serializer.errors}

def get_instructors():
    instructors = Instructor.objects.all()
    if not instructors.exists():
        raise ValidationError({"error": "No instructors found."})
    serializer = InstructorSerializers(instructors, many=True)
    return serializer.data

def get_instructor_by_id(instructor_id):
    try:
        instructor = Instructor.objects.get(instructor_id=instructor_id)
        serializer = InstructorSerializers(instructor)
        return serializer.data
    except Instructor.DoesNotExist:
        raise ValidationError({"error": "Instructor not found."})