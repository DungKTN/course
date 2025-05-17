from django.urls import path
from .views import CourseModuleListView, CourseModuleCreateView, CourseModuleDetailView

urlpatterns = [
    path('course_modules/', CourseModuleListView.as_view(), name='course-module-list'),
    path('course_modules/create', CourseModuleCreateView.as_view(), name='course-module-create'),
    path('course_modules/<int:course_module_id>', CourseModuleDetailView.as_view(), name='course-module-detail'),
    path('course_modules/<int:course_module_id>/update', CourseModuleDetailView.as_view(), name='course-module-update'),
    path('course_modules/<int:course_module_id>/delete', CourseModuleDetailView.as_view(), name='course-module-delete'),
]