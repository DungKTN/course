from django.urls import path
from .views import QnAAnswerListView

urlpatterns = [
    path('qna_answers/', QnAAnswerListView.as_view(), name='qna-answer-list'),
    path('qna_answers/create/', QnAAnswerListView.as_view(), name='qna-answer-create'),
    path('qna_answers/<int:answer_id>/update/', QnAAnswerListView.as_view(), name='qna-answer-update'),
    path('qna_answers/<int:answer_id>/delete/', QnAAnswerListView.as_view(), name='qna-answer-delete'),
]
