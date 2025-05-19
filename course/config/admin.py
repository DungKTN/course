from django.contrib import admin
from users.models import User
from admins.models import Admin
from courses.models import Course
from instructors.models import Instructor
from enrollments.models import Enrollment
from notifications.models import Notification
admin.site.register(User)
admin.site.register(Course)
admin.site.register(Instructor)
admin.site.register(Admin)
# admin.site.register(Order)
admin.site.register(Enrollment)
# admin.site.register(Payment)
# admin.site.register(Review)
admin.site.register(Notification)