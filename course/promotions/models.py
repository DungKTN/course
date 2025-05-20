from django.db import models
from admins.models import Admin

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
    applicable_courses = models.JSONField(blank=True, null=True)
    applicable_categories = models.JSONField(blank=True, null=True)
    admin_id = models.ForeignKey(Admin, on_delete=models.SET_NULL, related_name='promotions_created', null=True)
    status = models.CharField(max_length=10, choices=StatusChoices.choices, default=StatusChoices.ACTIVE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Promotions'

    def __str__(self):
        return f"{self.code} ({self.discount_type} - {self.promotion_id})"
