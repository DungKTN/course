from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .services import (
    create_promotion,
    delete_promotion,
    get_promotions_by_admin,
    get_promotion_by_id,
    update_promotion

)

class PromotionManagementView(APIView):
    def post(self, request):
        try:
            promotion = create_promotion(request.data)
            return Response(promotion, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({"error": e.detail}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request):
        try:
            if 'promotion_id' in request.query_params:
                promotion_id = request.query_params.get('promotion_id')
                promotion = get_promotion_by_id(promotion_id)
                return Response(promotion, status=status.HTTP_200_OK)
            elif 'admin_id' in request.query_params:
                admin_id = request.query_params.get('admin_id')
                promotions = get_promotions_by_admin(admin_id)
                return Response(promotions, status=status.HTTP_200_OK)
            else:
                return Response({"error": "promotion_id or admin_id is required"}, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError as e:
            return Response({"error": e.detail}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request):
        try:
            promotion_id = request.query_params.get('promotion_id')
            if not promotion_id:
                return Response({"error": "promotion_id is required"}, status=status.HTTP_400_BAD_REQUEST)
            result = delete_promotion(promotion_id)
            return Response(result, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"error": e.detail}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request):
        try:
            promotion_id = request.query_params.get('promotion_id')
            if not promotion_id:
                return Response({"error": "promotion_id is required"}, status=status.HTTP_400_BAD_REQUEST)
            promotion = update_promotion(promotion_id, request.data)
            return Response(promotion, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"error": e.detail}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
