from django.urls import path
from .views import InstructorListView, InstructorCreateView, InstructorDetailView

urlpatterns =[
    path('instructors/',InstructorListView.as_view(), name='instructor-list'),
    path('instructors/create',InstructorCreateView.as_view(), name='instructor-create'),
    path('instructors/<int:instructor_id>',InstructorDetailView.as_view(), name='instructor-detail'),   
    path('instructors/<int:instructor_id>/update',InstructorDetailView.as_view(), name='instructor-update'),
    path('instructors/<int:instructor_id>/delete',InstructorDetailView.as_view(), name='instructor-delete'),
]