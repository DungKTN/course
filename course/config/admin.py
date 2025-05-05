from django.contrib import admin
from users.models import User
from courses.models import Course
from instructors.models import Instructor
admin.site.register(User)
admin.site.register(Course)
admin.site.register(Instructor)
# admin.site.register(Order)
# admin.site.register(Enrollment)