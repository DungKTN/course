from django.urls import path
from .views import LearningProgressView
from rest_framework.routers import DefaultRouter
urlpatterns = [
   path('learning-progress/', LearningProgressView.as_view(), name='learning_progress'),
   path('learning-progress/<int:enrollment_id>/<int:lesson_id>/', LearningProgressView.as_view(), name='learning_progress_detail'),]