from rest_framework import serializers
from .models import Wishlist

class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = [
            'wishlist_id',
            'user_id',
            'course_id',
            'added_date'
        ]
        read_only_fields = [
            'wishlist_id'
        ]