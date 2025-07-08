from django .urls import path
from .views import QnAListView

urlpatterns = [
    path('qnas/', QnAListView.as_view(), name='qna-list'),
    path('qnas/create/', QnAListView.as_view(), name='qna-create'),
    path('qnas/<int:qna_id>/update/', QnAListView.as_view(), name='qna-update'),
    path('qnas/<int:qna_id>/delete/', QnAListView.as_view(), name='qna-delete'),
]