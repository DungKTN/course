from django.db import models
from users.models import User
from qnas.models import QnA

class QnAAnswer(models.Model):
    answer_id = models.AutoField(primary_key=True)
    qna_id = models.ForeignKey(QnA, on_delete=models.CASCADE, related_name='answwer_qna')
    answer = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answer_user')
    answered_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_accepted = models.BooleanField(default=False)
    likes = models.IntegerField(default=0)

    class Meta:
        db_table = 'QnAAnswers'

    def __str__(self):
        return f"Answer {self.answer_id}: QnA {self.qna_id}: User {self.user_id}"
