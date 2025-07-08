from django.urls import path
from .views import (InstructorEarningsView, 
                    InstructorEarningsByPayoutView)

urlpatterns = [
    path('instructor-earnings/', InstructorEarningsView.as_view(), name='instructor_earnings'),
    path('instructor-earnings/<str:payment_id>/', InstructorEarningsView.as_view(), name='generate_instructor_earnings_from_payment'),
    path('instructor-earnings/payout/<str:payout_id>/', InstructorEarningsByPayoutView.as_view(), name='update_instructor_earning_with_payout'),
]