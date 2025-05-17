from django.urls import path
from .views import (
    EnrollmentDetailView,
    EnrollmentManageByUserView,)

urlpatterns = [
    # path('enrollments/', EnrollmentListView.as_view(), name='enrollment-list'),
    path('enrollments/<int:pk>/', EnrollmentDetailView.as_view(), name='enrollment-detail'),
    path('enrollments/create/', EnrollmentManageByUserView.as_view(), name='enrollment-create'),
    # path('enrollments/update/<int:pk>/', EnrollmentUpdateView.as_view(), name='enrollment-update'),
    path('enrollments/', EnrollmentManageByUserView.as_view(), name='enrollment-manage'),

]