import cloudinary
import os
from django.conf import settings

print("🛠️ CLOUDINARY_CLOUD_NAME:", settings.CLOUDINARY_CLOUD_NAME)
print("🛠️ CLOUDINARY_API_KEY:", settings.CLOUDINARY_API_KEY)
print("🛠️ CLOUDINARY_API_SECRET:", settings.CLOUDINARY_API_SECRET)

cloudinary.config(
    cloud_name=settings.CLOUDINARY_CLOUD_NAME,
    api_key=settings.CLOUDINARY_API_KEY,
    api_secret=settings.CLOUDINARY_API_SECRET,
    secure=True
)
print("✅ Cloudinary configured!") 