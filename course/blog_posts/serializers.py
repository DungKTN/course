from rest_framework import serializers
from .models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = [
            'blog_post_id',
            'title',
            'content',
            'author_id',
            'created_at',
            'updated_at',
            'status',
            'tags',
            'category_id',
            'slug',
            'featured_image',
            'sumary',
            'published_at',
            'views',
            'allow_comments',
            'is_featured'
        ]
        read_only_fields = [
            'blog_post_id',
            'created_at',
        ]