from django.urls import path
from .views import CourseListView, CourseCreateView, CourseDetailView

urlpatterns = [
    path('courses/', CourseListView.as_view(), name='course-list'),
    path('courses/create', CourseCreateView.as_view(), name='course-create'),
    path('courses/<int:course_id>', CourseDetailView.as_view(), name='course-detail'),
    path('courses/<int:course_id>/update', CourseDetailView.as_view(), name='course-update'),
    path('courses/<int:course_id>/delete', CourseDetailView.as_view(), name='course-delete'),
]