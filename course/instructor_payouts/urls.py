from django.urls import path
from .views import (    InstructorPayoutView)

urlpatterns = [
    path('instructor-payouts/', InstructorPayoutView.as_view(), name='instructor_payouts_get_delete_detail'),
    path('instructor-payouts/delete/<int:payout_id>/', InstructorPayoutView.as_view(), name='delete_instructor_payout'),
]