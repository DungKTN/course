from django.db import models
from admins.models import Admin
from instructors.models import Instructor
from courses.models import Course
class Promotion(models.Model):
    class DiscountTypeChoices(models.TextChoices):
        PERCENTAGE = 'percentage', 'percentage'
        FIXED_AMOUNT = 'fixed', 'fixed'

    class StatusChoices(models.TextChoices):
        ACTIVE = 'active', 'active'
        INACTIVE = 'inactive', 'inactive'
        EXPIRED = 'expired', 'expired'

    promotion_id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    discount_type = models.CharField(max_length=20, choices=DiscountTypeChoices.choices)
    discount_value = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    usage_limit = models.IntegerField(blank=True, null=True)
    used_count = models.IntegerField(default=0)
    min_purchase = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    max_discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    applicable_courses = models.ManyToManyField(Course,blank=True,related_name="promotions")
    applicable_categories = models.ManyToManyField('categories.Category', blank=True, related_name="promotions")
# mã giảm giá admin áp cho payment , instructor áp cho danh mục khóa học và cho khóa học của người đó
# giảm giá danh mục thì chỉ có tác dụng với danh mục mà giảng viên đó quản lý
# giảm giá khóa học thì chỉ có tác dụng với khóa học mà giảng viên đó quản lý


    admin_id = models.ForeignKey(Admin, on_delete=models.SET_NULL, related_name='promotions_admin', null=True)
    instructor_id = models.ForeignKey(Instructor, on_delete=models.SET_NULL, related_name='promotions_instructor', null=True)
    
    status = models.CharField(max_length=10, choices=StatusChoices.choices, default=StatusChoices.ACTIVE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Promotions'

    def __str__(self):
        return f"{self.code} ({self.discount_type} - {self.promotion_id})"
