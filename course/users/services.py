from rest_framework.exceptions import ValidationError
from .models import User
from .serializers import Userserializers, UserUpdateBySelfSerializer
from config import settings
from django.contrib.auth.hashers import make_password, check_password
from datetime import datetime, timedelta
from django.utils import timezone
import jwt
JWT_SECRET = settings.SECRET_KEY
JWT_ALGORITHM = "HS256"

def create_user(data):
    serializer = Userserializers(data=data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        return user
    raise ValidationError(serializer.errors)

def update_user_by_selfself(user_id, data):
    try:
        user = User.objects.get(user_id=user_id)
    except User.DoesNotExist:
        raise ValidationError({"error": "User not found."})
    
    serializer = UserUpdateBySelfSerializer(user, data=data, partial=True)
    if serializer.is_valid(raise_exception=True):
        updated_user = serializer.save()
        return updated_user
    raise ValidationError(serializer.errors)
def update_user_by_admin(user_id, data):
    try:
        user = User.objects.get(user_id=user_id)
    except User.DoesNotExist:
        raise ValidationError({"error": "User not found."})
    
    serializer = Userserializers(user, data=data, partial=True)
    if serializer.is_valid(raise_exception=True):
        updated_user = serializer.save()
        return updated_user
    raise ValidationError(serializer.errors)


def delete_user(user_id):
    try:
        user = User.objects.get(user_id=user_id)
        user.delete()
        return {"message": "User deleted successfully."}
    except User.DoesNotExist:
        raise ValidationError({"error": "User not found."})

def validate_user_data(data):
    serializer = Userserializers(data=data)
    if serializer.is_valid():
        return {"message": "Data is valid."}
    return {"errors": serializer.errors}
def get_users():
        users = User.objects.all()
        if not users.exists():
            raise ValidationError({"error": "No users found."})
        serializer = Userserializers(users, many=True)
        return serializer.data
    
def get_user_by_id(user_id):
        try:
            user = User.objects.get(user_id=user_id)
            serializer = Userserializers(user)
            return serializer.data
        except User.DoesNotExist:
            raise ValidationError({"error": "User not found."})
def register(data):
    data['status'] = 'inactive'
    data['user_type'] = 'student'
    data['password_hash'] = make_password(data['password'])
    serializer = Userserializers(data=data)
    serializer.is_valid(raise_exception=True)
    return serializer.save()
def login(data):
    try:
        if data['username'] and data['password']:
            user = User.objects.get(username=data['username'])
    except User.DoesNotExist:
         raise ValidationError({"error": "User not found."})
    if not check_password(data['password'], user.password_hash):
        raise ValidationError({"error": "Invalid password."})
    if user.status != 'active':
        raise ValidationError({"error": "User is not active."})
    user.last_login = timezone.now()
    user.save()
    payload = {
        'user_id': user.user_id,
        'username': user.username,
        'email': user.email,
        'user_type': user.user_type,
        'exp': datetime.utcnow() + timedelta(minutes=30),
        "iat": datetime.utcnow()
    }
    access_token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    refresh_payload = {
        'user_id': user.user_id,
        'username': user.username,
        'email': user.email,
        'user_type': user.user_type,
        'exp': datetime.utcnow() + timedelta(days=3),
        "iat": datetime.utcnow()
    }
    refresh_token = jwt.encode(refresh_payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return {
        'access_token': access_token,
        'refresh_token': refresh_token,
        'user': {
            'user_id': user.user_id,
            'username': user.username,
            'email': user.email,
            'user_type': user.user_type,
        }
    }
def refresh_token(token):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=JWT_ALGORITHM)
        user = User.objects.get(user_id=payload['user_id'])
    except jwt.ExpiredSignatureError:
        raise ValidationError({"error": "Token has expired."})
    except jwt.InvalidTokenError:
        raise ValidationError({"error": "Invalid token."})
    except User.DoesNotExist:
        raise ValidationError({"error": "User not found."})

    new_payload = {
        'user_id': user.user_id,
        'username': user.username,
        'email': user.email,
        'user_type': user.user_type,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30),
        "iat": datetime.utcnow()
    }
    new_token = jwt.encode(new_payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return {
        'access_token': new_token,
        'message': "Token refreshed successfully.",
    }