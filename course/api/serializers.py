from rest_framework import serializers
from .models import User

class Userserializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =[
            'user_id',
            'username',
            'email',
            'full_name',
            'phone',
            'avatar',
            'address',
            'created_at',
            'last_login',
            'status',
            'user_type'
        ]
