from django.db import models
from admins.models import Admin

class SystemsSetting(models.Model):
    setting_id = models.AutoField(primary_key=True)
    setting_group = models.CharField(max_length=100)
    setting_key = models.CharField(max_length=100, unique=True)
    setting_value = models.TextField()
    description = models.CharField(max_length=255)
    admin_id = models.ForeignKey(Admin, on_delete=models.SET_NULL, related_name='settings_admin', null=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'SystemsSettings'

    def __str__(self):
        return f"{self.setting_key} = {self.setting_value}"