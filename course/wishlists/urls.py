from django.urls import path
from .views import WishlistListView, WishlistDetailView, UserWishlistView

urlpatterns = [
    path('wishlists/create/', WishlistListView.as_view(), name='wishlist-create'),
    path('wishlists/', WishlistListView.as_view(), name='wishlist-list'),
    path('wishlists/<int:wishlist_id>/', WishlistDetailView.as_view(), name='wishlist-detail'),
    path('wishlists/<int:wishlist_id>/', UserWishlistView.as_view(), name='user-wishlist'),
    path('wishlists/<int:wishlist_id>/delete/', WishlistListView.as_view(), name='wishlist-delete'),
    path('wishlists/<int:wishlist_id>/update/', WishlistListView.as_view(), name='wishlist-update'),
]