from django.urls import path
from .views import WishlistListView
urlpatterns = [
    path('wishlists/create/', WishlistListView.as_view(), name='wishlist-create'),
    path('wishlists/', WishlistListView.as_view(), name='wishlist-list'),
    path('wishlists/<int:wishlist_id>/delete/', WishlistListView.as_view(), name='wishlist-delete'),
    path('wishlists/<int:wishlist_id>/update/', WishlistListView.as_view(), name='wishlist-update'),
]