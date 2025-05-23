from rest_framework.exceptions import ValidationError
from .serializers import PromotionSerializer
from .models import Promotion
from admins.models import Admin
from users.models import User
from django.utils import timezone
from dateutil.parser import parse

def create_promotion(data):
    try:
        serializer = PromotionSerializer(data= data)
        try:
            adminCheck = Admin.objects.get(admin_id=data['admin_id'])
        except Admin.DoesNotExist:
                raise ValidationError({"error": "Admin not found."})
        try:
            end_date = parse(data['end_date'])
            if end_date < timezone.now():
                raise ValidationError({"error": "End date cannot be in the past."})
        except (ValueError, TypeError):  
            raise ValidationError({"error": "Invalid end date format."})
        
        if Promotion.objects.filter(code=data['code']).exists():
            raise ValidationError({"error": "Promotion code already exists."})
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return serializer.data
        raise ValidationError(serializer.errors)
    except Exception as e:
        raise ValidationError(f"Error creating promotion: {str(e)}")

def get_promotion_by_id(promotion_id):
    try:
        promotion = Promotion.objects.get(promotion_id=promotion_id)
        return PromotionSerializer(promotion).data
    except Promotion.DoesNotExist:
        raise ValidationError("Promotion not found")
    except Exception as e:
        raise ValidationError(f"Error retrieving promotion: {str(e)}")


def get_promotions_by_admin(admin_id):
    try:
        adminCheck = Admin.objects.get(admin_id=admin_id)
        if not adminCheck:
            raise ValidationError("Admin not found")
        promotions = Promotion.objects.filter(admin_id=adminCheck.admin_id)
        print("Promotions data:", admin_id)
        print("Promotions data:", promotions)
        return PromotionSerializer(promotions, many=True).data
    except Exception as e:
        raise ValidationError(f"Error retrieving promotions: {str(e)}")

def delete_promotion(promotion_id):
    try:
        promotion = Promotion.objects.get(promotion_id=promotion_id)
        promotion.delete()
        return {"message": "Promotion deleted successfully"}
    except Promotion.DoesNotExist:
        raise ValidationError("Promotion not found")
    except Exception as e:
        raise ValidationError(f"Error deleting promotion: {str(e)}")

def update_promotion(promotion_id, data):
    try:
        promotion = Promotion.objects.get(promotion_id=promotion_id)
    except Promotion.DoesNotExist:
        raise ValidationError({"error": "Promotion not found."})

    serializer = PromotionSerializer(promotion, data=data, partial=True)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return serializer.data
    raise ValidationError(serializer.errors)