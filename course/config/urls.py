"""
URL configuration for course project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('users.urls')),           # /api/users/
    path('api/', include('payments.urls')),        # /api/payments/
    # path('api/', include('reviews.urls')), 
    path('api/', include('courses.urls')),
    path('api/', include('instructors.urls')),
    path('api/', include('categories.urls')),
    path('api/', include('admins.urls')),
    path('api/', include('lessons.urls')),
    path('api/', include('coursemodules.urls')),
    path('api/', include('enrollments.urls')),
    path('api/', include('learning_progress.urls')),
    path('api/', include('reviews.urls')),
    path('api/', include('blog_posts.urls')),
    path('api/', include('lesson_attachments.urls')),
    path('api/', include('quiz_questions.urls')),
    path('api/', include('notifications.urls')),
    path('api/', include('promotions.urls')),
    path('api/', include('carts.urls')),
    path('api/', include('wishlists.urls')),
    path('api/', include('quiz_results.urls')),
    path('api/', include('qnas.urls')),
    path('api/', include('qna_answers.urls')),
    path('api/', include('forums.urls')),
    path('api/', include('forum_topics.urls')),
    path('api/', include('forum_comments.urls')),
    path('api/', include('systems_settings.urls')),
    path('api/', include('supports.urls')),
]