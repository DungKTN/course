from django.db import models

class InstructorLevel(models.Model):
    instructor_level_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)  # Ví dụ: Bronze, Silver, Gold
    description = models.TextField(blank=True, null=True)
    min_students = models.IntegerField(default=0)  # Hoặc doanh thu tối thiểu
    min_revenue = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    commission_rate = models.DecimalField(max_digits=5, decimal_places=2, default=30.00)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'InstructorLevels'

    def __str__(self):
        return f"{self.name} ({self.commission_rate}%)"
