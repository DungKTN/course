from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .services import (
    create_cart,
    get_cart_by_id,
    get_all_carts,
    update_cart,
    delete_cart,
    get_cart_by_user,
)

class CartListView(APIView):
    def get(self, request):
        carts = get_all_carts()
        return Response(carts, status=status.HTTP_200_OK)

    def post(self, request):
        try:
            cart = create_cart(request.data)
            return Response(cart, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({"errors": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, cart_id):
        try:
            cart = update_cart(cart_id, request.data)
            return Response(cart, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"errors": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, cart_id):
        try:
            result = delete_cart(cart_id)
            return Response(result, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"errors": str(e)}, status=status.HTTP_404_NOT_FOUND)

class CartDetailView(APIView):
    def get(self, request, cart_id):
        try:
            cart = get_cart_by_id(cart_id)
            return Response(cart, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"errors": str(e)}, status=status.HTTP_404_NOT_FOUND)
        
class UserCartView(APIView):
    def get(self, request, user_id):
        try:
            cart = get_cart_by_user(user_id)
            return Response(cart, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"errors": str(e)}, status=status.HTTP_404_NOT_FOUND)