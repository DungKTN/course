from django.urls import path
from .views import QuizResultListView

urlpatterns = [
    path('quiz_results/', QuizResultListView.as_view(), name='quiz-results-list'),
    path('quiz_results/create/', QuizResultListView.as_view(), name='quiz-results-create'),
    path('quiz_results/<int:quiz_result_id>/update/', QuizResultListView.as_view(), name='quiz-results-update'),
    path('quiz_results/<int:quiz_result_id>/delete/', QuizResultListView.as_view(), name='quiz-results-delete'), 
]