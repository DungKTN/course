from django.urls import path
from .views import UserListView, UserCreateView, UserDetailView, UserRegisterView, UserLoginView

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/create', UserCreateView.as_view(), name='user-create'),
    path('users/<int:user_id>', UserDetailView.as_view(), name='user-detail'),
    path('users/<int:user_id>/update', UserDetailView.as_view(), name='user-update'),
    path('users/<int:user_id>/delete', UserDetailView.as_view(), name='user-delete'),
    path('users/register', UserRegisterView.as_view(), name='user-register'),
    path('users/login', UserLoginView.as_view(), name='user-login'),

]