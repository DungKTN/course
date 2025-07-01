from django.urls import path
from .views import ForumTopicListView

urlpatterns = [
    path('forum_topics/', ForumTopicListView.as_view(), name='forum-topic-list'),
    path('forum_topics/create/', ForumTopicListView.as_view(), name='forum-topic-create'),
    path('forum_topics/<int:topic_id>/update/', ForumTopicListView.as_view(), name='forum-topic-update'),
    path('forum_topics/<int:topic_id>/delete/', ForumTopicListView.as_view(), name='forum-topic-delete'),
]