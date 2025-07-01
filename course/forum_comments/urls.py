from django.urls import path
from .views import ForumCommentListView

urlpatterns = [
    path('forum_comments/', ForumCommentListView.as_view(), name='forum-comment-list'),
    path('forum_comments/create/', ForumCommentListView.as_view(), name='forum-comment-create'),
    path('forum_comments/<int:comment_id>/update/', ForumCommentListView.as_view(), name='forum-comment-update'),
    path('forum_comments/<int:comment_id>/delete/', ForumCommentListView.as_view(), name='forum-comment-delete'),
]