from django.urls import path
from .views import ForumListView

urlpatterns = [
    path('forums/', ForumListView.as_view(), name='forum-list'),
    path('forums/create/', ForumListView.as_view(), name='forum-create'),
    path('forums/<int:forum_id>/update/', ForumListView.as_view(), name='forum-update'),
    path('forums/<int:forum_id>/delete/', ForumListView.as_view(), name='forum-delete'),
]