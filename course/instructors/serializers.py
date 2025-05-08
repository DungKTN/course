from rest_framework import serializers
from .models import Instructor
from users.models import User
from users.serializers import Userserializers  # Giả sử bạn đã có serializer cho User

class InstructorSerializers(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='user', write_only=True
    )  # Thêm trường user_id để nhận pk
    user = Userserializers(read_only=True)
    class Meta:
        model = Instructor
        fields = [
            'instructor_id',
            'user_id',  # Sử dụng user_id để tạo/ghi
            'user',  # Trả về thông tin user đầy đủ khi đọc
            'bio',
            'specialization',
            'qualification',
            'experience',
            'social_links',
            'rating',
            'total_students',
            'total_courses',
            'payment_info'
        ]
        extra_kwargs = {
            'user': {'read_only': True},  # Chỉ đọc cho trường user
            'total_students': {'read_only': True},
            'total_courses': {'read_only': True},
        }