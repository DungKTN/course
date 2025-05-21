from django.urls import path
from .views import ReviewListView, ReviewDetailView
urlpatterns = [
    path('reviews/', ReviewListView.as_view(), name='review-list'),
    path('reviews/create/', ReviewListView.as_view(), name='review-create'),
    path('reviews/update/<int:review_id>/', ReviewListView.as_view(), name='review-update'),
    path('reviews/delete/<int:review_id>/', ReviewListView.as_view(), name='review-delete'),
    path('reviews/<int:review_id>/', ReviewDetailView.as_view(), name='review-detail'),
    
]