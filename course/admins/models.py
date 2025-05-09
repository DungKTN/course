from django.db import models
from users.models import User  

class Admin(models.Model):
    admin_id = models.AutoField(primary_key=True)  
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)  
    department = models.CharField(max_length=100)  
    role = models.CharField(max_length=100, default='none')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  

    class Meta:
        db_table = 'Admin'  

    def __str__(self):
        return f"{self.user.username} - {self.role}"