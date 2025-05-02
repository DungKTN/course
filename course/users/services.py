from rest_framework.exceptions import ValidationError
from .models import User
from .serializers import Userserializers

def create_user(data):
    serializer = Userserializers(data=data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        return user
    raise ValidationError(serializer.errors)

def update_user(user_id, data):
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