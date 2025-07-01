from django.db import models
from forums.models import Forum
from users.models import User

class ForumTopic(models.Model):
    topic_id = models.AutoField(primary_key=True)
    forum_id = models.ForeignKey('forums.Forum', on_delete=models.CASCADE, related_name='topics_forum')
    title = models.CharField(max_length=255)
    content = models.TextField()
    user_id = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='topics_user', db_column='user_id')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    status = models.CharField(max_length=10, choices=[
        ('active', 'active'),
        ('locked', 'locked'),
        ('deleted', 'deleted'),
    ], default='locked')
    is_pinned = models.BooleanField(default=False)

    class Meta:
        db_table = 'ForumTopics'

    def __str__(self):
        return f"Topic {self.topic_id}: {self.title} by {self.user_id}"