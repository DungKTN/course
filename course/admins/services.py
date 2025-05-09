from .models import Admin
from .serializers import AdminSerializer
from rest_framework.exceptions import ValidationError
def updateAdminInfo (admin_id, data):
    try:
        admin = Admin.objects.get(admin_id=admin_id)
    except Admin.DoesNotExist:
        raise ValidationError({"error": "Admin not found."})
    print("Admin found:", admin)
    serializer = AdminSerializer(admin, data=data, partial=True)
    if serializer.is_valid(raise_exception=True):
        updated_admin = serializer.save()
        return updated_admin
    raise ValidationError(serializer.errors)
    

def delete_admin(admin_id):
    try:
        admin = Admin.objects.get(admin_id=admin_id)
        admin.delete()
        return {"message": "Admin deleted successfully."}
    except Admin.DoesNotExist:
        raise ValidationError({"error": "Admin not found."})
    
def get_admins():
    admins = Admin.objects.all()
    if not admins.exists():
        raise ValidationError({"error": "No admins found."})
    serializer = AdminSerializer(admins, many=True)
    return serializer.data
def get_admin_by_id(admin_id):
    try:
        admin = Admin.objects.get(admin_id=admin_id)
        serializer = AdminSerializer(admin)
        return serializer.data
    except Admin.DoesNotExist:
        raise ValidationError({"error": "Admin not found."})
def create_admin(data):
    serializer = AdminSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        admin = serializer.save()
        return admin
    raise ValidationError(serializer.errors)