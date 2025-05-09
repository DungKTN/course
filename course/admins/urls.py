from django.urls import path
from .views import (
    AdminManagementView,
    AdminDetailView,
    AdminListView,
)

urlpatterns = [
    path('admins/<int:admin_id>/update', AdminManagementView.as_view(), name='admin-update'),
    path('admins/<int:admin_id>/delete', AdminManagementView.as_view(), name='admin-delete'),
    path('admins/', AdminListView.as_view(), name='admin-list'),
    path('admins/create', AdminManagementView.as_view(), name='admin-create'),
    path('admins/<int:admin_id>', AdminDetailView.as_view(), name='admin-detail'),
]

