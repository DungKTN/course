from .models import User
from django.utils import timezone

def create_user(data):
    user = User.objects.create(
        username=data['username'],
        email=data['email'],
        password_hash=data['password_hash'],
        full_name=data['full_name'],
        phone=data.get('phone'),
        avatar=data.get('avatar'),
        address=data.get('address'),
        status=data.get('status', User.StatusChoices.ACTIVE),
        user_type=data['user_type'],
        created_at=timezone.now()
    )
    return user
