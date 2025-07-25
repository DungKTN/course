from django.db import models
from users.models import User
from admins.models import Admin
from supports.models import Support

class SupportReply(models.Model):
    reply_id = models.AutoField(primary_key=True)
    support_id = models.ForeignKey(Support, on_delete=models.CASCADE, related_name='replies')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='support_replies')
    admin_id = models.ForeignKey(Admin, on_delete=models.CASCADE, related_name='support_replies')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Reply by {self.support_id} to {self.message} at {self.created_at}'