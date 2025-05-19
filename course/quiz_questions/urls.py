from django.urls import path
from .views import (
    QuizQuestionManagementView,
    QuizQuestionDetailView,
    QuizQuestionListView,
)
urlpatterns = [
    path('questions/', QuizQuestionListView.as_view(), name='quiz-question-list'),
    path('questions/<int:question_id>/', QuizQuestionManagementView.as_view(), name='quiz-question-list'),
    path('questions/<int:question_id>/', QuizQuestionDetailView.as_view(), name='quiz-question-detail'),
    path('questions/create/', QuizQuestionManagementView.as_view(), name='quiz-question-create'),
    path('questions/update/<int:question_id>/', QuizQuestionManagementView.as_view(), name='quiz-question-update'),
    path('questions/delete/<int:question_id>/', QuizQuestionManagementView.as_view(), name='quiz-question-delete'),
]