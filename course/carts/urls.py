from django.urls import path
from .views import CartListView, CartDetailView

urlpatterns = [
    path('carts/create/', CartListView.as_view(), name='cart-create'),
    path('carts/', CartListView.as_view(), name='cart-list'),
    path('carts/<int:cart_id>/', CartDetailView.as_view(), name='cart-detail'),
    path('carts/<int:user_id>/', CartListView.as_view(), name='user-cart'),
    path('carts/<int:cart_id>/delete/', CartListView.as_view(), name='cart-delete'),
    path('carts/<int:cart_id>/update/', CartListView.as_view(), name='cart-update'),
]