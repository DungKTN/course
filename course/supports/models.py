from django.db import models
from users.models import User
from admins.models import Admin

class Support(models.Model):
    STATUS_CHOICES = [
        ('open', 'open'),
        ('in_progress', 'in_progress'),
        ('resolved', 'resolved'),
        ('closed', 'closed'),
    ]

    PRIORITY_CHOICES = [
        ('low', 'low'),
        ('medium', 'medium'),
        ('high', 'high'),
        ('urgent', 'urgent'),
    ]

    support_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='support_user')
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Open')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    admin_id = models.ForeignKey(Admin, on_delete=models.SET_NULL, null=True, blank=True, related_name='support_admin')

    class Meta:
        db_table = 'Support'
        ordering = ['-created_date']

    def __str__(self):
        return f"{self.subject} (#{self.support_id}) - {self.status}"
