from django.urls import path
from .views import (
    QuizQuestionManagementView
)
urlpatterns = [
    path('questions/', QuizQuestionManagementView.as_view(), name='quiz-question-list'),
    path('questions/create/', QuizQuestionManagementView.as_view(), name='quiz-question-create'),
    path('questions/update/<int:question_id>/', QuizQuestionManagementView.as_view(), name='quiz-question-update'),
    path('questions/delete/<int:question_id>/', QuizQuestionManagementView.as_view(), name='quiz-question-delete'),
]