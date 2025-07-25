from .views import UploadFileView
from django.urls import path
urlpatterns = [
    path('cloudinary/upload/', UploadFileView.as_view(), name='upload_file'),
    path('cloudinary/delete/', UploadFileView.as_view(), name='delete_file'),]