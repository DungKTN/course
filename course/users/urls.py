from django.urls import path
from .views import   UserDetailView, UserRegisterView, UserLoginView, UserUpdateView, UserManagementView    

urlpatterns = [
    path('users/', UserManagementView.as_view(), name='user-list'),
    path('users/create', UserManagementView.as_view(), name='user-create'),
    path('users/<int:user_id>/delete', UserManagementView.as_view(), name='user-delete'),
    path('users/<int:user_id>/update', UserManagementView.as_view(), name='user-update-admin'),
    path('users/<int:user_id>', UserDetailView.as_view(), name='user-detail'),
    path('users/<int:user_id>/updateinfo', UserUpdateView.as_view(), name='user-update'),
    path('users/register', UserRegisterView.as_view(), name='user-register'),
    path('users/login', UserLoginView.as_view(), name='user-login'),

]