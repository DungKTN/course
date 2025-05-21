from django.contrib import admin
from users.models import User
from admins.models import Admin
from courses.models import Course
from instructors.models import Instructor
from enrollments.models import Enrollment
from reviews.models import Review
from blog_posts.models import BlogPost
admin.site.register(BlogPost)
admin.site.register(User)
admin.site.register(Course)
admin.site.register(Instructor)
admin.site.register(Admin)
# admin.site.register(Order)
admin.site.register(Enrollment)
admin.site.register(Review)
