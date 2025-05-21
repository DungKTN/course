from django.urls import path
from .views import (
    AdminBlogPostView,
    ClientBlogPostView,
)

urlpatterns = [
    path('admin/blog-posts/', AdminBlogPostView.as_view(), name='admin-blog-posts'),
    path('client/blog-posts/', ClientBlogPostView.as_view(), name='client-blog-posts'),
    path('admin/blog-posts/create/', AdminBlogPostView.as_view(), name='admin-blog-post-create'),
    path('admin/blog-posts/update/<int:blog_post_id>/', AdminBlogPostView.as_view(), name='admin-blog-post-update'),
    path('admin/blog-posts/delete/<int:blog_post_id>/', AdminBlogPostView.as_view(), name='admin-blog-post-delete'),
    path('client/blog_posts/increase_views/<int:blog_post_id>/', ClientBlogPostView.as_view(), name='client-blog-post-increase-views'),
]