from django.urls import path
from .views import CreateVnpayPaymentView, VnpayReturnView
# , VnpayReturnView, CreatePaymentRecordView

urlpatterns = [
    path('vnpay/create/', CreateVnpayPaymentView.as_view(), name='vnpay-create'),
    path('vnpay/return/', VnpayReturnView.as_view(), name='vnpay-return'),
    # path('vnpay/return/', VnpayReturnView.as_view(), name='vnpay-return'),
    # path('payment/create/', CreatePaymentRecordView.as_view(), name='payment-create'),
]
