from rest_framework import serializers
from .models import Category

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Category
        extra_kwargs = {
            "name": {
                "required": True,
                "error_messages": {
                    "blank": "Name cannot be blank",
                    "null": "Name cannot be null",
                    "required": "Name is required",
                },
            },
            "description": {
                "required": False,
                "error_messages": {
                    "blank": "Description cannot be blank",
                    "null": "Description cannot be null",
                },
            },
        }