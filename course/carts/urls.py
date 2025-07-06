from django.urls import path
from .views import CartListView

urlpatterns = [
    path('carts/create/', CartListView.as_view(), name='cart-create'),
    path('carts/', CartListView.as_view(), name='cart-list'),
    path('carts/<int:cart_id>/delete/', CartListView.as_view(), name='cart-delete'),
    path('carts/<int:cart_id>/update/', CartListView.as_view(), name='cart-update'),
]