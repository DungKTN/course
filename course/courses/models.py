from django.db import models
from instructors.models import Instructor
from categories.models import Category


class Course(models.Model):
    class Level(models.TextChoices):
        BEGINNER = 'Beginner'
        INTERMEDIATE = 'Intermediate'
        ADVANCED = 'Advanced'
        ALL_LEVELS = 'All Levels'

    class Status(models.TextChoices):
        DRAFT = 'Draft'
        PENDING = 'Pending'
        PUBLISHED = 'Published'
        REJECTED = 'Rejected'
        ARCHIVED = 'Archived'
    course_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    instructor_id = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='courses',null=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='courses', null=True)
    subcategory_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='courses', null=True)
    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    discount_start_date = models.DateTimeField(blank=True, null=True)
    discount_end_date = models.DateTimeField(blank=True, null=True)
    level = models.CharField(
        max_length=20,
        choices=Level.choices,
        default=Level.ALL_LEVELS
    )
    language = models.CharField(max_length=50, default='Tiếng Việt')
    duration = models.IntegerField(help_text="Thời lượng tính bằng phút", blank=True, null=True)
    total_lessons = models.IntegerField(default=0)
    requirements = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.DRAFT
    )
    is_featured = models.BooleanField(default=False)
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)
    rating = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    total_reviews = models.IntegerField(default=0)
    total_students = models.IntegerField(default=0)
    certificate = models.BooleanField(default=False)

    class Meta:
        db_table = 'Courses'
        
def __str__(self):
    return f"Course {self.course_id} - {self.instructor.full_name}"



