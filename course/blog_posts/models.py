from django.db import models
from users.models import User
from categories.models import Category

class BlogPost(models.Model):
    class StatusChoices(models.TextChoices):
        DRAFT = 'draft', 'draft'
        PUBLISHED = 'published', 'published'
        ARCHIVED = 'archived', 'archived'
    blog_post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    author_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.DRAFT
    )
    tags = models.JSONField(null=True, blank=True)
    category_id = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='blog_posts',
        null=True,
        blank=True
    )
    slug = models.SlugField(max_length=255, unique=True)
    featured_image = models.CharField(max_length=255, null=True, blank=True)
    sumary = models.TextField(null=True, blank=True)
    published_at = models.DateTimeField(null=True, blank=True)
    views = models.IntegerField(default=0)
    allow_comments = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        db_table = "blog_posts"
    
    def __str__(self):
        return f"BlogPost {self.title} - {self.status}"


