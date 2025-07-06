from django.db import models
from users.models import User
from forum_topics.models import ForumTopic

class ForumComment(models.Model):
    STATUS_CHOICES = [
        ('active', 'active'),
        ('deleted', 'deleted'),
    ]

    comment_id = models.AutoField(primary_key=True)
    topic_id = models.ForeignKey(ForumTopic, on_delete=models.CASCADE, related_name='comments_topic')
    content = models.TextField()
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name='comments_user')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    parent_comment = models.ForeignKey('self',null=True,blank=True,on_delete=models.SET_NULL,related_name='replies')
    likes = models.IntegerField(default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='aactive')
    is_best_answer = models.BooleanField(default=False)

    class Meta:
        db_table = 'ForumComments'

    def __str__(self):
        return f"Comment {self.comment_id} on Topic {self.topic_id} by User {self.user_id}"
