from django.urls import path
from .views import LessonListView, LessonCreateView, LessonDetailView
urlpatterns = [
    path('lessons/', LessonListView.as_view(), name='lesson-list'),
    path('lessons/create', LessonCreateView.as_view(), name='lesson-create'),
    path('lessons/<int:lesson_id>', LessonDetailView.as_view(), name='lesson-detail'),
    path('lessons/<int:lesson_id>/update', LessonDetailView.as_view(), name='lesson-update'),
    path('lessons/<int:lesson_id>/delete', LessonDetailView.as_view(), name='lesson-delete'),
]