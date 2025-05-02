from django.urls import path
from .views import UserListView
from .views import UserCreateView

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('create/', UserCreateView.as_view(), name='user-create'),
]